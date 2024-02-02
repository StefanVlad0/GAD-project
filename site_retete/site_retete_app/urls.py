from django.urls import path
from . import views
from .views import adauga_reteta

urlpatterns = [
    path("", views.home, name="home"),
    path('adauga-reteta/', adauga_reteta, name='adauga_reteta')
]