
from rest_framework import serializers

from cv.models.diplome import Diplome

   
class DiplomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diplome
        exclude = ['profil']