from rest_framework import viewsets, generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comic, ComicHasSerie, Serie, User, Rol
from .serializers import ComicSerializer, ComicHasSerieSerializer, SerieSerializer, UserSerializer, RolSerializer, AuthenticationSerializer
from django.contrib.auth import login
from social_django.utils import psa

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


class Authentication(generics.CreateAPIView):
    serializer_class = AuthenticationSerializer

    def post(self, request, format=None):
        serializer = AuthenticationSerializer(data=request.data)
        backend =social_core.backends.google.GoogleOAuth2()
        if serializer.is_valid():
            token = serializer.data['idtoken']
            user = register_by_access_token(request,backend, token=token)
            #user = request.backend.do_auth(token)
            if user:
                newUser = User(id=user.id, nombre='Test', rol='1')
                userserializer = UserSerializer(newUser)
                userserializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@psa('social:complete')
def register_by_access_token(request, backend, token):
    backend = social_core.backends.google.GoogleOAuth2()
    user =  request.backend.do_auth(access_token=token, backend=backend)

    if user:
        return user
    else:
        return None
