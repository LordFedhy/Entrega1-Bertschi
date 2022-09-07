from django.urls import path
from empresa.views import *

uurlpatterns = [
    #path("padre/",padre),
    path('cliente1/',cliente1,name="clientes"),
    path('provedor1/',provedor1,name="provedores"),
    path('mercaderia1/',mercaderia1,name="mercaderia"),

    #path("", inicio, name="inicio"),
    path("padre/",padre, name="padre"),
    #path("cursoformulario/",cursoformulario, name="cursoformulario"),
    ]