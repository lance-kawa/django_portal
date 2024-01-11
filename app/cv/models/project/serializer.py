
from rest_framework import serializers

from cv.models.project import Project

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        exclude = ['profil']