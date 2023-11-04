from rest_framework import viewsets
from django.contrib.auth.models import User
from .models import Profile
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]
