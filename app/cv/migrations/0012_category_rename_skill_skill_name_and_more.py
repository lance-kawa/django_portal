# Generated by Django 4.2.7 on 2023-12-04 15:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0011_remove_project_tags_skill_logo_alter_project_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='category',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='tech',
        ),
        migrations.AddField(
            model_name='skill',
            name='categorya',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='skills', to='cv.category'),
        ),
    ]