from django.shortcuts import render

# Create your views here.
import datetime

def index(request):
    days = [1, 2, 3, 4, 5]
    days_time = 2000
    now = datetime.datetime.now()
    return render(request,'scenario.html', {'now': now, "days": days, "days_time": days_time})