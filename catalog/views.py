from django.shortcuts import render
from catalog.models import Plant, WaterDat
from django.views.generic.edit import CreateView
from django.http import HttpResponse
import csv
# Create your views here.


def index(request) :
	
	context = {
		 'plants' : Plant.objects.all(),
		'test' : 2,
	}
	return render(request, 'index.html', context=context)
	
def charts(request) :
	
	context = {
		 'plants' : Plant.objects.all(),
		'WaterDat' : WaterDat.objects.all()
	}
	return render(request, 'charts.html', context=context)	
	
def get_min(request) :
	if request.method == 'GET':
		plant_id = request.GET['plant_type']
		
	if plant_id :
		this_plant = Plant.objects.get(plant_type = plant_id)
		min_water = this_plant.min_water
		
	return HttpResponse(min_water)

def get_max(request) :
	if request.method == 'GET':
		plant_id = request.GET['plant_type']
		
	if plant_id :
		this_plant = Plant.objects.get(plant_type = plant_id)
		max_water = this_plant.max_water
		
	return HttpResponse(max_water)

def save(request) :
	if request.method == 'GET':
		plant_id = request.GET['plant_type']
		min__water = request.GET['min_water']
		max__water = request.GET['max_water']
		
		new_plant = Plant(plant_type = plant_id, min_water = min__water, max_water = max__water)
		new_plant.save()
	return HttpResponse('success!')

def write(request):
    # Create the HttpResponse object with the appropriate CSV header.
	plant_1 = Plant.objects.get(plant_type = request.GET['plant_1_id'])
	plant_2 = Plant.objects.get(plant_type = request.GET['plant_2_id'])
	
	with open('water.csv', 'w', newline='') as f:
		writer = csv.writer(f)
		writer.writerow(['plant_type', 'min_water', 'max_water'])
		writer.writerow([plant_1.plant_type , plant_1.min_water, plant_1.max_water])
		writer.writerow([plant_2.plant_type , plant_2.min_water, plant_2.max_water])
	
	response = HttpResponse('Sucsess')
	return response