from django.db import models
#from django.utils.encoding import smart_unicode

# Create your models here.

class Usuario(models.Model):
    nombre = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Preguntas(models.Model):
    pregunta = models.CharField(max_length=1000)
    respuesta = models.CharField(max_length=1000)

    def __str__(self):
        return u'%s %s' % (self.pregunta, self.respuesta)

class Hermano(models.Model):
    usuario = models.ForeignKey(Usuario)
    nombre_hermano = models.CharField(max_length=100)
    telefono = models.IntegerField(max_length=20)
    nacimiento = models.DateField()

    def __str__(self):
       return self.nombre_hermano


class Estadisticas(models.Model):
    pregunta = models.ForeignKey(Preguntas)
    nombre_hermano = models.ForeignKey(Hermano)
    contador = models.IntegerField()
    lugar = models.IntegerField()

    def __str__(self):
       return u'%s %s %s' % (self.lugar, self.nombre_hermano, self.contador)

