from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField("Категория", max_length=300)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    id_obj = models.PositiveIntegerField()
    content_object = GenericForeignKey('type', 'id_obj')

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = "Лайк"
        verbose_name_plural = "Лайки"


class Posts(models.Model):
    title = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение", upload_to='post/')
    discription = models.TextField("Описание")
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    likes = GenericRelation(Like)

    def add_like(self, request, post, is_like):
        old_like = LikeDislike.objects.filter(user=request.user, post=post)
        if old_like:
            like = LikeDislike.objects.get(user=request.user, post=post)
            if like.like_or_dislike == 'like' and is_like == 'like':
                like.delete()
                self.like -= 1
                post.save()
            elif like.like_or_dislike == 'dislike' and is_like == 'dislike':
                like.delete()
                self.dislike -= 1
                post.save()
            elif like.like_or_dislike == 'like' and is_like == 'dislike':
                like.like_or_dislike = 'dislike'
                like.save()
                self.dislike += 1
                self.like -= 1
                post.save()
            elif like.like_or_dislike == 'dislike' and is_like == 'like':
                like.like_or_dislike = "like"
                like.save()
                self.dislike -= 1
                self.like += 1
                post.save()
        else:
            new_like = LikeDislike(user=request.user, post=post, like_or_dislike=is_like)
            print(is_like)
            new_like.save()
            if is_like == 'like':
                self.like += 1
                post.save()
            elif is_like == 'dislike':
                self.dislike += 1
                post.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"



class LikeDislike(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    like_or_dislike_choice = (("Like", "like"), ('Dislike', 'dislike'), (None, 'None'))
    like_or_dislike = models.CharField(max_length=10, choices=like_or_dislike_choice, default=None, null=True)


class Comments(models.Model):
    description = models.TextField("Комментарии")
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Statistics(models.Model):
    like_stat = models.IntegerField(default=0)
    dislike_stat = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def calculate_stat(self, request,):
        posts = Posts.objects.all()
        if posts:
            for i in posts:
                if i.author == request.user:
                    self.like_stat += i.like
                    self.dislike_stat += i.dislike
            new_statistic = Statistics(like_stat=self.like_stat, dislike_stat=self.dislike_stat , user=request.user)
            new_statistic.save()

            return "{}{}".format(self.like_stat, self.dislike_stat)
        else:
            print('У этого поьзователя нет постов!')

    def __str__(self):
        return "{}{}".format(self.like_stat, self.dislike_stat)