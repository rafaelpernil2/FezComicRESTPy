from rest_framework import serializers
from .models import Comic,ComicHasSerie,Rol,Serie,User,Like,Comentario

class ComicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comic
        fields = '__all__'   

class ComicHasSerieSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComicHasSerie
        fields = '__all__'

class SerieSerializer(serializers.ModelSerializer):        
    class Meta:
        model = Serie
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):        
    class Meta:
        model=Rol
        fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comentario
        fields = '__all__'

class AuthenticationSerializer(serializers.Serializer):
    idtoken = serializers.CharField(required=True)