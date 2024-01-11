
from django.contrib import admin
from django.forms import ModelForm
from django.forms.widgets import TextInput
from portfolio.interface.profil_admin import ProfilAdmin, SubProfilAdmin
from cv.models.profil import Profil
from cv.models.theme import Theme
from cv.models.diplome import Diplome
from cv.models.experience import Experience
from cv.models.project import Project
from cv.models.skill import Skill, Category


class ProfilAdmin(ProfilAdmin):
    list_display = ['firstname', 'name', 'profil_picture'] 

class DiplomeAdmin(SubProfilAdmin):
    list_display = ('title', 'profil_name', 'graduation_date', 'school', 'place')
    search_fields = ['title', 'profil_name']

class ExperienceAdmin(SubProfilAdmin):
    list_display = ('entreprise', 'poste', 'profil_name')

class CategoryAdmin(SubProfilAdmin):
    list_display = ['name', 'skills'] 

    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class SkillAdmin(SubProfilAdmin):
    list_display = ['name', 'profil_name', 'category'] 

class ProjectAdmin(SubProfilAdmin):
    list_display = ['title', 'profil_name'] 


class ThemeForm(ModelForm):
    class Meta:
        model = Theme
        fields = "__all__"
        widgets = {
            'primary_color': TextInput(attrs={'type': 'color'}),
            'secondary_color': TextInput(attrs={'type': 'color'}),
            'extra_color': TextInput(attrs={'type': 'color'}),
            'default_font_color': TextInput(attrs={'type': 'color'}),
            'secondary_font_color': TextInput(attrs={'type': 'color'}),
        }
        
class ThemeAdmin(SubProfilAdmin):
    form = ThemeForm

admin.site.register(Theme, ThemeAdmin)
admin.site.register(Profil, ProfilAdmin)
admin.site.register(Diplome, DiplomeAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Category, CategoryAdmin)
