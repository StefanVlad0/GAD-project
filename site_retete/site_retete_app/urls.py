from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import adauga_reteta, reteta_view, reteta_update, reteta_delete, importa_reteta, logout_view

urlpatterns = [
    path("", views.home, name="home"),
    path('adauga-reteta/', adauga_reteta, name='adauga_reteta'),
    path('reteta/<int:id_reteta>', reteta_view, name='reteta_view'),
    path('reteta_modifica/<int:id_reteta>', reteta_update, name='reteta_update'),
    path('reteta_delete/<int:id_reteta>', reteta_delete, name='reteta_delete'),
    path('importa-reteta/', importa_reteta, name='importa_reteta'),
    path('login/', include('django.contrib.auth.urls'), {'next_page': '/'}, name='login'),
    path('login/', LoginView.as_view(template_name='not_log.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]