from django.db import models
from cv.models.profil import Profil
from modeltranslation.translator import register, TranslationOptions

class Experience(models.Model):
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE, related_name='experiences')
    entreprise = models.CharField(max_length=255)
    poste = models.CharField(max_length=255)
    place = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.poste
    
@register(Experience)
class ExperienceTranslation(TranslationOptions):
    fields = ('poste', 'description',)  # specify fields to translate