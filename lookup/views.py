# This is my views.py file
from django.shortcuts import render

# Create your views here.

def home(request):
	import json
	import requests

	if request.method == "POST":
			zipcode = request.POST['zipcode']

			api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=25&API_KEY=8025EE3D-F9D7-4D97-9C1E-BA89A1A7F258")

			try: 
				api = json.loads(api_request.content)
			except Exception as e:
				api = "Error..."

			# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=~distance~&API_KEY=8025EE3D-F9D7-4D97-9C1E-BA89A1A7F258
			return render(request, 'home.html',{'api': api})

	else:

		api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=25&API_KEY=8025EE3D-F9D7-4D97-9C1E-BA89A1A7F258")

		try: 
			api = json.loads(api_request.content)
		except Exception as e:
			api = "Error..."

		# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=20002&distance=~distance~&API_KEY=8025EE3D-F9D7-4D97-9C1E-BA89A1A7F258
		return render(request, 'home.html',{'api': api})


def about(request):
	return render(request, 'about.html',{})