from django.shortcuts import render
from .calc import one_route, clc
from .get import req

# Create your views here.
import datetime

def index(request):
    print(one_route(req("https://dt.miet.ru/ppo_it_final", "9e83w26h"), 0))
    days = one_route(req("https://dt.miet.ru/ppo_it_final/judge", "9e83w26h"), 0)[0]
    days_time = 1000

    power = [80]
    press = [150]
    temp  = [20]


    content = {
    "days": list(days), 
    
    'power': power,
    'press': press,
    'temp': temp,
    'population': [2000],
    'resourses': [1, 2],
    'resourses_time': 1000,
    'resourses_nows_time': 3000,
    'power_time': 200,
    'press_time': 200,
    'temp_time': 300,
    'population_time': 400,
    "days_time": days_time,}


    return render(request,'scenario.html', content)