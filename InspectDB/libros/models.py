# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Autores(models.Model):
    nombre = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    nacionalidad = models.CharField(max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'autores'


class Libros(models.Model):
    titulo = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    fecha_publicacion = models.DateField(blank=True, null=True)
    autor = models.ForeignKey(Autores, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'libros'
