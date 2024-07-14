from django.urls import path
from .views import moisture_list

urlpatterns =[
    path('', moisture_list, name='moisture_list'),
]