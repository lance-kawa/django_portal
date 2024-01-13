from django.db import models
from cv.models.profil import Profil
from modeltranslation.translator import register, TranslationOptions

class Project(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='static/media/project_images/', blank=True)
    description = models.TextField(blank=True)
    github = models.URLField(blank=True)
    demo = models.URLField(blank=True)

    def __str__(self):
        return self.title

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='static/media/project_images/')

    def __str__(self):
        return self.image.url

@register(Project)
class ProjectTranslation(TranslationOptions):
    fields = ('description',)  # specify fields to translate