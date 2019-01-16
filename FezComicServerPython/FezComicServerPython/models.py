# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Comic(models.Model):
    #id = models.AutoField(primary_key=true)
    nombre = models.CharField(unique=True, max_length=60)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    foto = models.TextField(blank=True, null=True)
    anotacion_privada = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comic'


class ComicHasSerie(models.Model):
    id_comic = models.ForeignKey(Comic, models.DO_NOTHING, db_column='id_comic', primary_key=True)
    id_serie = models.ForeignKey('Serie', models.DO_NOTHING, db_column='id_serie')
    anotacion_publica = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comic_has_serie'
        unique_together = (('id_comic', 'id_serie'),)


class Rol(models.Model):
    #id = models.AutoField(primary_key=true)
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'rol'


class Serie(models.Model):
    #id = models.AutoField(primary_key=true)
    nombre = models.CharField(unique=True, max_length=60)
    anotacion_privada = models.CharField(max_length=200, blank=True, null=True)
    genero = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'serie'


class User(models.Model):
    id = models.CharField(primary_key=True, max_length=45)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    rol = models.ForeignKey(Rol, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user'
