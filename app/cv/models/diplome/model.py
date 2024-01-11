from django.db import models
from cv.models.profil import Profil

class Diplome(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='diplomes')
    title = models.CharField(max_length=255)
    graduation_date = models.DateField(blank=True, null=True)
    school = models.CharField(max_length=255, blank=True)
    place = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title
    
