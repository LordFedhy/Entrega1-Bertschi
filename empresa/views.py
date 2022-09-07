from cgitb import text
from django.http import HttpResponse
from django.shortcuts import render

from .models import*
# Create your views here.
#def padre(request):
    #return render(request, "padre.html")

def cliente1(request):
    if request.method=="POST":
        cliente1=Cliente(request.POST["nombre"],request.POST["apellido"],request.POST["email"],request.POST["telefono"])
        cliente1.save()
        return render(request,"inicio.html")
    return render(request,"clientes.html")

def mercaderia1(request):
    if request.method=="POST":
        mercaderia1=Mercaderia(request.POST["nombre"],request.POST["codigo_barra"],request.POST["cantidad"])
        mercaderia1.save()
        return render(request,"inicio.html")
    return render(request,"mercaderia.html")
    

def provedor1(request):
    if request.method=="POST":
        provedor1=Provedor(request.POST["nombre"],request.POST["telefono"],request.POST["email"])
        provedor1.save()
        return render(request,"inicio.html")
    return render(request, "provedores.html")

def inicio(request):
    return render(request,"inicio.html")

def padre(request):
    return render(request,"padre.html")


