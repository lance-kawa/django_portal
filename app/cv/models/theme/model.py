from django.db import models
from cv.models.profil.model import Profil
from django.core.validators import RegexValidator
from django.core.validators import RegexValidator


class ColorField(models.CharField):
    COLORS_REGEX = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
    COLORS_ERROR_MESSAGE = 'Enter a valid color value in hexadecimal format (e.g. #RRGGBB or #RGB).'

    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 7
        kwargs['validators'] = [RegexValidator(regex=self.COLORS_REGEX, message=self.COLORS_ERROR_MESSAGE)]
        super().__init__(*args, **kwargs)


class Theme(models.Model):
    name = models.CharField(max_length=255)
    primary_color = ColorField(blank=True, default='#FFFFFF')
    secondary_color = ColorField(blank=True, default='#000000')
    extra_color = ColorField(blank=True, default='#808080')
    default_font_color = ColorField(blank=True, default='#000000')
    secondary_font_color = ColorField(blank=True, default='#FFFFFF')
    category_order = models.TextField(blank=True, default='')
    skill_display = models.TextField(blank=True, default='')
    profil = models.OneToOneField(Profil, on_delete=models.CASCADE, related_name='theme')
    

    def __str__(self):
        return self.name







    
