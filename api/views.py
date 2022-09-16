from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from AppPelis.models import Pelicula
from .serializers import UserSerializer, GroupSerializer, PeliculaSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PeliculaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaSerializer
    permission_classes = [permissions.IsAuthenticated]
	