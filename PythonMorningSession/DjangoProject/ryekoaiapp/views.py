from django.shortcuts import render
from .models import SoilMoistureReading
# Create your views here.

def moisture_list(request):
    readings = SoilMoistureReading.objects.all().order_by('-timestamp')# descending order of timestamp
    return render(request, 'ryekoapp/moisture_list.html', {'readings': readings})