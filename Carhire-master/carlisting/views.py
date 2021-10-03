from django.shortcuts import render
from .models import CarMake, CarType, carInstance, CarModel, Car, carOwner
from django.views.generic import ListView

# Create your views here.
def index(request):
    """""view function to specify the site homepage"""

    #generate a count of all the cars in the system

    cars_count = Car.objects.all().count()
    car_instance = carInstance.objects.all().count()

    #count the number of available cars
    cars_available = carInstance.objects.filter(status__exact = 'a').count()

    #counr the number of toyotas
    toyotas_available = CarMake.objects.filter(car_make__exact='Toyota').count()

    #Context specifies how the data will be presented in the rendered view
    context = {
        'cars_count': cars_count,
        'car_instance': car_instance,
        'cars_available': cars_available,
        'toyotas_available':toyotas_available,
    }
    return render(request, 'index.html', context=context)

#def allCars(request):
 #   """View all the cars in the system"""
 #   owner = carOwner.objects;





class CarList(ListView):
        model = Car
