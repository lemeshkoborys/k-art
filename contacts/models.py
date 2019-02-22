from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class FeedbackCategory(models.Model):

    class Meta:
        db_table = 'feedback_categories'
        verbose_name = 'Категория вопроса'
        verbose_name_plural = 'Категории вопросов'

    title = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        verbose_name='Название категории вопроса/обратной связи'
    )

    content = models.TextField(
        null=True,
        blank=True,
        verbose_name='Описание категории (только для администрации)'
    )

    def __str__(self):
        return self.title


class Feedback(models.Model):

    class Meta:
        db_table = 'feedbacks'
        verbose_name = 'Обратная связь'
        verbose_name_plural = 'Обратные связи'

    category = models.ForeignKey(
        FeedbackCategory,
        on_delete=models.CASCADE,
        related_name='feedbacks',
        verbose_name='Категория вопроса',
        blank=True
    )

    name = models.CharField(
        max_length=120,
        null=False,
        blank=False,
        verbose_name='Имя'
    )

    email = models.EmailField(
        null=False,
        blank=False
    )

    phone = PhoneNumberField(
        blank=True,
        null=True,
        verbose_name='Номер телефона (опционально)'
    )

    content = models.TextField(
        null=False,
        blank=False,
        verbose_name='Текст сообщения'
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Создано'
    )