from django.urls import path
from . import views
from .views import adauga_reteta, reteta_view, reteta_update, reteta_delete, importa_reteta

urlpatterns = [
    path("", views.home, name="home"),
    path('adauga-reteta/', adauga_reteta, name='adauga_reteta'),
    path('reteta/<int:id_reteta>', reteta_view, name='reteta_view'),
    path('reteta_modifica/<int:id_reteta>', reteta_update, name='reteta_update'),
    path('reteta_delete/<int:id_reteta>', reteta_delete, name='reteta_delete'),
    path('importa-reteta/', importa_reteta, name='importa_reteta'),
]