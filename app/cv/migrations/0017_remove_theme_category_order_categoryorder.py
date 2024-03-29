# Generated by Django 4.2.7 on 2023-12-06 13:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0016_remove_theme_demo_remove_theme_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='theme',
            name='category_order',
        ),
        migrations.CreateModel(
            name='CategoryOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.PositiveIntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.category')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cv.theme')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
