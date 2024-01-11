
from rest_framework import serializers
from cv.models.theme import Theme

class ThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        exclude = ['profil']