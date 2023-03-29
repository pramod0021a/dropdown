from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
     path('', views.person, name = "person"),
     path('cities', views.cities, name = "cities")
]