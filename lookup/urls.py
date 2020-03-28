from django.urls import path
from . import views

urlpatterns = [
	path('',views.home, name='home'),
	path('about.html',views.about, name='about'),
	path('sobre.html',views.sobre, name='sobre'),
]


