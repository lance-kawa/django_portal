from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfilViewSet

router = DefaultRouter()
router.register(r'me', ProfilViewSet, basename='profil')

urlpatterns = [
    path('', include(router.urls)),
]
