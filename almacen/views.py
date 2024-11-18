from django.shortcuts import render
from .models import Articulos

# Create your views here.

def almacen(request):

    articulos=Articulos.objects.all()

    return render(request, "almacen/almacen.html", {"articulos":articulos})