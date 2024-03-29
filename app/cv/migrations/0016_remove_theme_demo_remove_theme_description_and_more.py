# Generated by Django 4.2.7 on 2023-12-06 13:10

import cv.models.theme.model
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0015_theme'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='demo',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='description',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='github',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='image',
        ),
        migrations.RemoveField(
            model_name='theme',
            name='title',
        ),
        migrations.AddField(
            model_name='theme',
            name='category_order',
            field=models.ManyToManyField(to='cv.category'),
        ),
        migrations.AddField(
            model_name='theme',
            name='default_font_color',
            field=cv.models.theme.model.ColorField(blank=True, default='#000000', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
        migrations.AddField(
            model_name='theme',
            name='extra_color',
            field=cv.models.theme.model.ColorField(blank=True, default='#808080', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
        migrations.AddField(
            model_name='theme',
            name='name',
            field=models.CharField(default='theme', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='theme',
            name='primary_color',
            field=cv.models.theme.model.ColorField(blank=True, default='#FFFFFF', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
        migrations.AddField(
            model_name='theme',
            name='secondary_color',
            field=cv.models.theme.model.ColorField(blank=True, default='#000000', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
        migrations.AddField(
            model_name='theme',
            name='secondary_font_color',
            field=cv.models.theme.model.ColorField(blank=True, default='#FFFFFF', max_length=7, validators=[django.core.validators.RegexValidator(message='Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).', regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$')]),
        ),
    ]
