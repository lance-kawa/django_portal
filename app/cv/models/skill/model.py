from django.db import models
from cv.models.profil import Profil

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Skill(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='static/media/skill_images/', blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='skills', blank=True, null=True)


    def __str__(self):
        return self.name
    