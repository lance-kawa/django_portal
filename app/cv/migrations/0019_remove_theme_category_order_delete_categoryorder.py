# Generated by Django 4.2.7 on 2023-12-06 13:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0018_theme_category_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='category_order',
        ),
        migrations.DeleteModel(
            name='CategoryOrder',
        ),
    ]