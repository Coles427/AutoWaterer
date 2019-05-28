from django.shortcuts import render
from catalog.models import Plant
# Create your views here.
def index(request) :
	
	context = {
		 'plants' : Plant.objects.all(),
		'test' : 2,
	}
	return render(request, 'index.html', context=context)