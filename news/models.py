from django.db import models


class Post(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок новости'
    )

    short_description = models.TextField(
        verbose_name='Краткое описание новости'
    )

    description = models.TextField(
        verbose_name='Текст новости'
    )

    image = models.ImageField(
        upload_to='images/news/',
        verbose_name='Изображение'
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
