from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
	path('', views.index, name = 'index'),
	path('charts', views.charts, name = 'charts'),
	url(r'^get_min/$', views.get_min, name='get_min'),
	url(r'^get_max/$', views.get_max, name='get_max'),
	url(r'^save/$', views.save, name='save'),
	url(r'^write/$', views.write, name='write'),
]