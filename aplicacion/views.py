from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "aplicacion/base.html")

def cliente(request):
    return render(request, "aplicacion/cliente.html")

def top(request):
    return render(request, "aplicacion/top.html")

def camisas(request):
    return render(request, "aplicacion/camisas.html")

def clienteForm(request):
    return render(request, "aplicacion/clienteForm.html")