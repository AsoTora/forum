from django.db import models

# Create your models here.


class Category(models.Model):

    name = models.CharField("Категория поста", max_length=150)
    discription = models.TextField("Описание", max_length=255)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class User(models.Model):
    name = models.CharField("Имя", max_length=25)
    last_name = models.CharField("Фамилия", max_length=25)
    age = models.PositiveSmallIntegerField("Возраст", default=0)
    discription = models.TextField("Описание", max_length=200)
    image = models.ImageField("Изображение", upload_to='user/')
    email = models.EmailField("Почта", unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

class Post(models.Model):
    title = models.CharField("Название", max_length=255)
    image = models.ImageField("Изображение", upload_to='post/')
    discription = models.TextField("Описание", max_length=500)
    user = models.ForeignKey(User, verbose_name='user', related_name='post_creator', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, verbose_name='category', on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"

class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Rating(models.Model):

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда" )
    post = models.ForeignKey(Post, on_delete=models.CharField, verbose_name="пост")

    def __str__(self):
        return f"{self.star}-{self.post}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"

class Commemt(models.Model):

    email = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Текст", max_length=5000)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True)
    post = models.ForeignKey(Post, verbose_name="пост", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}-{self.post}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
