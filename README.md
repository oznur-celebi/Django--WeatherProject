<!-- Please update value in the {}  -->

<h1 align="center">TODO App</h1>


<div align="center">
  <h3>
    <a href="https://{your-demo-link.your-domain}">
      Demo
    </a>
     | 
    <a href="https://{your-url-to-the-solution}">
      Project
    </a>
 
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
- [Built With](#built-with)
- [Features](#features)
- [How to use](#how-to-use)
- [Acknowledgements](#acknowledgements)
- [Contact](#contact)

<!-- OVERVIEW -->

## Overview

![screenshot](https://user-images.githubusercontent.com/16707738/92399059-5716eb00-f132-11ea-8b14-bcacdc8ec97b.png)

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- HTML
- CSS
- Django

## How To Use

<!-- This is an example, please update according to your application -->

To clone and run this application, you'll need [Git](https://git-scm.com) 
```bash
# Clone this repository
$ git clone https://github.com/aaron-clarusway/django_TODO_APPS.git

# Install dependencies
    $ python -m venv env
    > env/Scripts/activate (for win OS)
    $ source env/bin/activate (for macOs/linux OS)
    $ pip install django

# Run the app
$ python manage.py runserver

# add  the endpoint url to views.py
# import the Library requests and pprint to see nice jsondata in your Terminal
import requests
from decouple import config
from pprint import pprint
def index(request):
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    city ="Berlin"
    response = requests.get(url.format(city, config("API_KEY")))
    content = response.json()
    pprint(content)
    pprint(type(content))
    return render(request, "weatherapp/index.html")

# Create a Model to register the Cities used to be in the App
# models.py

class City(models.Model):
    name =models.CharField(max_length=100)
    def __str__(self):
        return self.name
# Register your Model into the admin.py
from .models import City
admin.site.register(City)

# import the model into the views.py page to get he data from database
from .models import City
# and get the all datas from our database

cities = City.objects.all()

#-----views.py------#

def index(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    for city in cities:
        print(city)
        response = requests.get(url.format(city, config("API_KEY")))
        content = response.json()
        return render(request, "weatherapp/index.html")

# Create a dictionary named data or whatelse you want, these are the datas , that will be used in your app 

data = {
            "city":city.name,
            "temp" : content["main"]["temp"],
            "desc" : content["weather"][0]["description"],
            "icon" : content["weather"][0]["icon"],
        }

# 1 -Create a  empty list named city_data und 2- append data into--in views.py

def index(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric"
    city_data =[] # 1
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
        city_data.append(data)#2
        pprint(city_data)
      context ={ #We use the Context in our Template
        "city_data": city_data
        }
    return render(request, "weatherapp/index.html", context)

#  Create a div in the index.html to show datas in city_data
   <div>
   <h1>Weather App</h1> 
   {% for city  in city_data %}
   {{city.city}}<br>
   {{city.temp}}<br>  
   {{city.desc}}<br>
   <hr>
   {% endfor %}
   </div> 

## Acknowledgements
- Information for your projects

## Contact

- Website [your-website.com](https://{your-web-site-link})
- GitHub [@your-username](https://{github.com/your-usermame})

- Linkedin [@your-linkedin](https://{linkedin.com/your-username})
- Twitter [@your-twitter](https://{twitter.com/your-username})
