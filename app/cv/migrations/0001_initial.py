# Generated by Django 4.2.7 on 2023-11-23 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profil_picture', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('name', models.CharField(max_length=100)),
                ('firstname', models.CharField(max_length=100)),
                ('tel', models.CharField(max_length=20)),
                ('linkedin', models.URLField()),
                ('github', models.URLField()),
                ('website', models.URLField()),
                ('intro', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=255)),
                ('tech', models.BooleanField()),
                ('category', models.CharField(choices=[('known', 'Known'), ('fluent', 'Fluent'), ('interested', 'Interested'), ('tool', 'Tool'), ('hobby', 'Hobby')], max_length=10)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='cv.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('github', models.URLField()),
                ('demo', models.URLField()),
                ('tags', models.JSONField(blank=True, null=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='cv.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('entreprise', models.CharField(max_length=255)),
                ('poste', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='experiences', to='cv.profil')),
            ],
        ),
        migrations.CreateModel(
            name='Diplome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('graduation_date', models.DateField()),
                ('school', models.CharField(max_length=255)),
                ('place', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('profil', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='diplomes', to='cv.profil')),
            ],
        ),
    ]
