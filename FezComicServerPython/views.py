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
  def delete(self, request, pk, format=None):
    serie = self.get_object(pk)
    serie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class RolViewSet(viewsets.ModelViewSet):
  queryset = Rol.objects.all()
  serializer_class = RolSerializer

class UserViewSet(viewsets.ModelViewSet):
  queryset = User.objects.all()
  serializer_class = UserSerializer  
