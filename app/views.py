from django.shortcuts import render_to_response, render, RequestContext, get_list_or_404
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.template import loader, Context
from app.models import Preguntas, Hermano, Estadisticas, Usuario
import random

def index(request):
    return render_to_response("base.html")

#--------------------------------- HTML_INICIO ----------------------------------------#
def inicio(request):
    template = loader.get_template("inicio.html")
    contexto = Context()
    return HttpResponse(template.render(contexto))
    #Antigua forma de hacer el return
    #return render_to_response('inicio.html', locals(), context_instance = RequestContext(request))

def preguntas(request):
    cpu = random.choice(range(1,10))
    valor = int(cpu)
    pregunta = Preguntas.objects.filter(id=valor)
    respuesta = Preguntas.objects.filter(id=valor)
    template = loader.get_template("preguntas.html")
    contexto = Context({'pregunta': pregunta}, {'respuesta':respuesta})
    return HttpResponse(template.render(contexto))

def estadisticas(request):
    estadistica = Estadisticas.objects.all()
    template = loader.get_template("estadisticas.html")
    contexto = Context({'estadistica': estadistica})
    return HttpResponse(template.render(contexto))

def nuevapregunta(request):
    template = loader.get_template("nuevapregunta.html")
    contexto = Context()
    return HttpResponse(template.render(contexto))


def login(request):
    template = loader.get_template("login.html")
    contexto = Context()
    return HttpResponse(template.render(contexto))

#--------------------------------- HTML_FIN ----------------------------------------#

#--------------------------------- FUNCIONES_INICIO ----------------------------------------#

#--------------------------------- FUNCIONES_FIN ----------------------------------------#