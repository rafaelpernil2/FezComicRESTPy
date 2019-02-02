from rest_framework import viewsets, generics, status
from rest_framework.parsers import FormParser
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Comic, ComicHasSerie, Serie, User, Rol, Comentario,Like
from .serializers import ComicSerializer, ComicHasSerieSerializer, SerieSerializer, UserSerializer, RolSerializer, AuthenticationSerializer,ComentarioSerializer,LikeSerializer
import urllib.request
import json


class GetSeriesByComic(generics.ListAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        comic = self.kwargs['id_comic']
        series = ComicHasSerie.objects.filter(id_comic=comic).values_list('id_serie', flat=True)
        series = list(series)
        result = Serie.objects.filter(pk__in=series)
        
        return result


class GetUserByToken(generics.RetrieveAPIView):
    serializer_class = UserSerializer

    def get(self, request, pk, format=None):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=" + pk
        response = urllib.request.urlopen(url).read()
        user_id = json.loads(response.decode('utf-8'))['sub']
        serializer = UserSerializer(User.objects.get(pk=user_id))
        return Response(serializer.data)



class GetComicsBySerie(generics.ListAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        serie = self.kwargs['id_serie']
        comics = ComicHasSerie.objects.filter(id_serie=serie).values_list('id_comic', flat=True)
        comics = list(comics)
        result = Comic.objects.filter(pk__in=comics)
        
        return result
        
class GetComicHasSerie(APIView):
    serializer_class = ComicHasSerieSerializer

    def get(self, request, *args, **kwargs):
        serie = self.kwargs['id_serie']
        comic = self.kwargs['id_comic']
        comichasseries = ComicHasSerie.objects.filter(id_serie=serie,id_comic=comic).values_list('id',flat=True)
        ids = list (comichasseries)
        result = ComicHasSerie.objects.get(pk = ids[0])
        serializer  = ComicHasSerieSerializer(result)
        return Response(serializer.data)
    
    def put(self, request,*args, **kwargs):
        serie = self.kwargs['id_serie']
        comic = self.kwargs['id_comic']
        comichasseries = ComicHasSerie.objects.filter(id_serie=serie,id_comic=comic).values_list('id',flat=True)
        if comichasseries:
            ids = list (comichasseries)
            comichasserie = ComicHasSerie.objects.get(pk = ids[0])
            serializer = ComicHasSerieSerializer(comichasserie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ComicHasSerieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        serie = self.kwargs['id_serie']
        comic = self.kwargs['id_comic']
        comichasseries = ComicHasSerie.objects.filter(id_serie=serie,id_comic=comic).values_list('id',flat=True)
        ids = list (comichasseries)
        comichasserie = ComicHasSerie.objects.get(pk = ids[0])
        comichasserie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetComicsByNombre(generics.ListAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        nombre = self.kwargs['nombre']
        return Comic.objects.filter(nombre=nombre)

class GetComentariosByComic(generics.ListAPIView):
    serializer_class = ComentarioSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        comic = self.kwargs['id_comic']
        return Comentario.objects.filter(comic=comic)

class GetLikesByComic(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        comic = self.kwargs['id_comic']
        return Like.objects.filter(comic=comic)

class LikesCountByComic(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self,request,*args, **kwargs):
        result = Like.objects.filter(comic= self.kwargs['id_comic']).count()
        return Response(result)


class GetLikeByUserAndComic(generics.ListAPIView):
    serializer_class = LikeSerializer

    def get(self,request,*args, **kwargs):
        result = Like.objects.get(comic= self.kwargs['id_comic'], user = self.kwargs['id_user'])
        serializer = LikeSerializer(result)
        return Response(serializer.data)


class ComicViewSet(viewsets.ModelViewSet):
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer
    def put(self, request, pk, format=None):
        comic = self.get_object(pk)
        serializer = ComicSerializer(comic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    def put(self, request, pk, format=None):
        comentario = self.get_object(pk)
        serializer = ComentarioSerializer(comentario, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = LikeSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ComicHasSerieViewSet(viewsets.ModelViewSet):
    queryset = ComicHasSerie.objects.all()
    serializer_class = ComicHasSerieSerializer

    def put(self, request,format=None):
        comichasseries = ComicHasSerie.objects.filter(id_serie=request.data['id_serie'],id_comic=request.data['id_comic']).values_list('id',flat=True)
        if comichasseries:
            ids = list (comichasseries)
            comichasserie = ComicHasSerie.objects.get(pk = ids[0])
            serializer = ComicHasSerieSerializer(comichasserie, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = ComicHasSerieSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




    


class SerieViewSet(viewsets.ModelViewSet):
    queryset = Serie.objects.all()
    serializer_class = SerieSerializer

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = SerieSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RolViewSet(viewsets.ModelViewSet):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = RolSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def put(self, request, pk, format=None):
        obj = self.get_object(pk)
        serializer = UserSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Authentication(generics.CreateAPIView):
    serializer_class = AuthenticationSerializer
    parser_classes = (FormParser,)

    def post(self, request, format=None):
        data= request.data
        
        token = data['idtoken']
        url = "https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=" + token
        response = urllib.request.urlopen(url).read()
        user_id = json.loads(response.decode('utf-8'))['sub']
        user_name = json.loads(response.decode('utf-8'))['name']

        
        
        if user_id:
            try:
                User.objects.get(pk=user_id)
                newUser = User.objects.get(pk=user_id)
                return Response(status=status.HTTP_201_CREATED)
            except User.DoesNotExist:
                newUser = User(id=user_id, nombre=user_name, rol=Rol.objects.get(pk=1))
                userserializer = UserSerializer(newUser)
                serializer = UserSerializer(data=userserializer.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
        else:
            return Response(userserializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
