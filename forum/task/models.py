from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Like(models.Model):
    user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class Posts(models.Model):
    title = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение", upload_to='post/')
    discription = models.TextField("Описание")
    published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, verbose_name='Просмотры')
    category = models.ForeignKey(Category, verbose_name='Категории', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    likes = GenericRelation(Like)

    @property
    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"



class LikeDislike(models.Model):
    like = models.BooleanField()
    dislike = models.BooleanField()
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # def __str__(self):
    #     return self


class Comments(models.Model):
    description = models.CharField("Комментарии", max_length=1000)
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    author_comment = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, )

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"