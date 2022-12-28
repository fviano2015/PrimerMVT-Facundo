from django.shortcuts import render
from django.http import HttpResponse
from familiares.models import Familiares
# Create your views here.

def crear_familiar(request):
    familiar_1 = Familiares.objects.create(nombre = "Cande" , estatura = 1.79 , casado = False)
    familiar_2 = Familiares.objects.create(nombre = "Fernanda" , estatura = 1.65 , casado = True)
    familiar_3 = Familiares.objects.create(nombre = "Guillermo" , estatura = 1.90 , casado = True)
    return HttpResponse("familiar agregado con éxito")

def lista_familiares(request):
    tdos_los_familiares = Familiares.objects.all()
    print(tdos_los_familiares)
    context = {'familiares' : tdos_los_familiares}
    return render(request, 'lista_familiares.html', context = context)