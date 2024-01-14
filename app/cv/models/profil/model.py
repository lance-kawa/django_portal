from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from modeltranslation.translator import register, TranslationOptions

class Profil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profil')
    firstname = models.CharField(max_length=100) 
    name = models.CharField(max_length=100) 
    profil_picture = models.ImageField(upload_to='static/media/profil_pictures/', blank=True, null=True)
    cv_picture = models.ImageField(upload_to='static/media/cv_pictures/', blank=True, null=True)
    bg_picture = models.ImageField(upload_to='static/media/cv_pictures/', blank=True, null=True)
    cv = models.FileField(upload_to='static/media/cv/', blank=True, null=True)
    email = models.EmailField(unique=True)
    address = models.TextField(blank=True, null=True) 
    tel = models.CharField(max_length=20, blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True) 
    github = models.URLField(blank=True, null=True) 
    website = models.URLField(blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self): 
        return f"{self.name} {self.firstname}"

@register(Profil)
class ProfilTranslation(TranslationOptions):
    fields = ('intro', 'job')  # specify fields to translate

@receiver(post_save, sender=User)
def assign_profil_add_permission(sender, instance, created, **kwargs):
    if created:
        instance.is_staff = True
        instance.save()
        content_type = ContentType.objects.get_for_model(Profil)
        add_permission = Permission.objects.get(codename='add_profil', content_type=content_type)
        instance.user_permissions.add(add_permission)
