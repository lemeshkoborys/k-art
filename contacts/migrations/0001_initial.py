# Generated by Django 2.1.7 on 2019-02-21 13:43

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, verbose_name='Номер телефона (опционально)')),
                ('content', models.TextField(verbose_name='Текст сообщения')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Обратная связь',
                'verbose_name_plural': 'Обратные связи',
                'db_table': 'feedbacks',
            },
        ),
        migrations.CreateModel(
            name='FeedbackCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название категории вопроса/обратной связи')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Описание категории (только для администрации)')),
            ],
            options={
                'verbose_name': 'Категория вопроса',
                'verbose_name_plural': 'Категории вопросов',
                'db_table': 'feedback_categories',
            },
        ),
        migrations.AddField(
            model_name='feedback',
            name='category',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='feedbacks', to='contacts.FeedbackCategory', verbose_name='Категория вопроса'),
        ),
    ]
