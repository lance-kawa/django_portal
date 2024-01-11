
from rest_framework import serializers

from cv.models.experience import Experience

   
class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        exclude = ['profil']