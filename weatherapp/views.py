# from django.shortcuts import render
# import requests
# from decouple import config

# # Create your views here.
# def index(request) :
#     url ="https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
#     city ="Berlin"
#     response =requests.get(url.format(city, config("API_KEY")))
#     content =response.json()
#     print(content)
#     return render(request, "weatherapp/index.html")

from multiprocessing import context
from django.shortcuts import render
import requests
from decouple import config
from pprint import pprint

from manage import main
from .models import City


def index(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    city_data =[]
    for city in cities:
        print(city)
        response = requests.get(url.format(city, config("API_KEY")))
        content = response.json()
        pprint(content)
        data = {
            "city":city.name,
            "temp" : content["main"]["temp"],
            "desc" : content["weather"][0]["description"],
            "icon" :content["weather"][0]["icon"],
        }
        city_data.append(data)
        pprint(city_data)
    context ={
        "city_data": city_data
        }
    return render(request, "weatherapp/index.html", context)
