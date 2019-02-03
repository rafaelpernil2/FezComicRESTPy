"""FezComicServerPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'comics',views.ComicViewSet)
router.register(r'comichasseries',views.ComicHasSerieViewSet)
router.register(r'series',views.SerieViewSet)
router.register(r'users',views.UserViewSet)
router.register(r'roles',views.RolViewSet)
router.register(r'likes',views.LikeViewSet)
router.register(r'comentarios',views.ComentarioViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path(r'auth',views.Authentication.as_view()),
    path('admin/', admin.site.urls),
    re_path('comichasseries/comics/(?P<id_serie>.+)/$',views.GetComicsBySerie.as_view()),
    re_path('comichasseries/comichasserie/(?P<id_comic>.+)/(?P<id_serie>.+)/$',views.GetComicHasSerie.as_view()),
    re_path('comichasseries/series/(?P<id_comic>.+)/$',views.GetSeriesByComic.as_view()),
    re_path('comics/comicsbynombre/(?P<nombre>.+)/$',views.GetComicsByNombre.as_view()),
    re_path('comics/(?P<pk>.+)/$',views.DeleteComic.as_view()),
    re_path('likes/likesbycomic/(?P<id_comic>.+)/$',views.GetLikesByComic.as_view()),
    re_path('likes/likesbycomic/count/(?P<id_comic>.+)$',views.LikesCountByComic.as_view()),
    re_path('likes/likebyuserandcomic/(?P<id_user>.+)/(?P<id_comic>.+)/$',views.LikeByUserAndComic.as_view()),
    re_path('comentarios/comentariosbycomic/(?P<id_comic>.+)/$',views.GetComentariosByComic.as_view()),
    re_path('users/getuserbytoken/(?P<pk>.+)/$',views.GetUserByToken.as_view()),
]
