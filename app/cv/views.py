from rest_framework import viewsets
from cv.models.profil import Profil, ProfilSerializer
from rest_framework import permissions

class ProfilViewSet(viewsets.ModelViewSet):
    serializer_class = ProfilSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # This ensures that a user can only access their own profile
        return Profil.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # This ensures that a profile is linked to the current user when created
        serializer.save(user=self.request.user)
