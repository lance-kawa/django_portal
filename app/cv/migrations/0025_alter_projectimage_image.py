# Generated by Django 4.2.9 on 2024-01-13 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0024_projectimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectimage',
            name='image',
            field=models.ImageField(upload_to='static/media/project_images/'),
        ),
    ]
