from rest_framework import viewsets
from rest_framework.views import APIView
from .models import Comic,ComicHasSerie,Serie,User,Rol
from .serializers import ComicSerializer,ComicHasSerieSerializer,SerieSerializer,UserSerializer,RolSerializer


class ComicViewSet(viewsets.ModelViewSet):
  queryset = Comic.objects.all()
  serializer_class = ComicSerializer

class ComicHasSerieViewSet(viewsets.ModelViewSet):
  queryset = ComicHasSerie.objects.all()
  serializer_class = ComicHasSerieSerializer

class SerieViewSet(viewsets.ModelViewSet):
  queryset = Serie.objects.all()
  serializer_class = SerieSerializer

class RolViewSet(viewsets.ModelViewSet):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer  
