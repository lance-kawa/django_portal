
from rest_framework import serializers
from cv.models.profil import Profil
from cv.models.experience import ExperienceSerializer
from cv.models.diplome import DiplomeSerializer
from cv.models.project import ProjectSerializer
from cv.models.skill import SkillSerializer

class ProfilSerializer(serializers.ModelSerializer):

    experiences = ExperienceSerializer(many=True, read_only=True)
    diplomes = DiplomeSerializer(many=True, read_only=True)
    projects = ProjectSerializer(many=True, read_only=True)
    skills = SkillSerializer(many=True, read_only=True)
    
    class Meta:
        model = Profil
        exclude = ['user']