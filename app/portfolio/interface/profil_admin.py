from django.contrib import admin
from cv.models.profil import Profil
from cv.models.profil.schema import SubProfil

class ProfilAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ['user'] 
        else:
            self.exclude = ()
        return super(ProfilAdmin, self).get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and not change:
            obj.user = request.user
        super().save_model(request, obj, form, change)

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return not Profil.objects.filter(user=request.user).exists()
    
    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.user == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.user == request.user
        return True

class SubProfilAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        if not request.user.is_superuser:
            self.exclude = ['profil']
        else:
            self.exclude = ()
        return super(SubProfilAdmin, self).get_form(request, obj, **kwargs)
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(profil=request.user.profil)

    def save_model(self, request, obj, form, change):
        if not request.user.is_superuser and not change:
            obj.profil = request.user.profil
        super().save_model(request, obj, form, change)

    def profil_name(self, obj: SubProfil):
        return obj.profil.firstname
    
    def has_add_permission(self, request):
        return True 
    
    def has_change_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.profil.user == request.user
        return True

    def has_delete_permission(self, request, obj=None):
        if obj is not None and not request.user.is_superuser:
            return obj.profil.user == request.user
        return True
    
    profil_name.short_description = 'Profil Name'

