from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Photo(models.Model):
    image = models.ImageField(
        upload_to='images/',
        verbose_name='Изображение'
    )
    album = models.ForeignKey(
        'index.PhotoAlbum',
        on_delete=models.CASCADE
    )


class PhotoAlbum(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name='Название альбома'
    )

    category = models.ForeignKey(
        'index.Category',
        on_delete=models.CASCADE,
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title

    def get_images(self):
        return Photo.objects.filter(album=self)


class Category(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Заголовок категории'
    )

    description = models.TextField(verbose_name='Описание категории')
    
    section = models.ForeignKey(
        'index.Section',
        on_delete=models.CASCADE,
        verbose_name='Секция к которой относится данная категория'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_album(self):
        return PhotoAlbum.objects.get(category=self)

    class Meta:
        db_table = 'Categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Section(models.Model):

    title = models.CharField(
        max_length=255,
        verbose_name='Загловок раздела'
    )

    order = models.PositiveIntegerField(
        verbose_name='Порядок отображения (1-4)',
        validators=[
            MinValueValidator(1, 'Order can\'t be less than 1'),
            MaxValueValidator(4, 'Order can\'t be more than 4')
        ],
        unique=True,
        blank=True
    )

    def get_categories(self):
        return Category.objects.filter(section=self).order_by('created_at')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
