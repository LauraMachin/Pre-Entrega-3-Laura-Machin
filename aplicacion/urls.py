from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="inicio"),

    path('cliente/', cliente, name="cliente"),
    path('top/', top, name="top"),
    path('camisas/', camisas, name="camisas"),    
    path('cliente_form/', clienteForm, name="cliente_form"),
]