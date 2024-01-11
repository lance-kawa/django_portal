
from rest_framework import serializers

from cv.models.skill import Skill

   
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        exclude = ['profil']