from django.urls import path
from . import views

urlpatterns = [
    # qnd a rota '' for acessada, ele deve utilizar a função views.index
    path('', views.index, name='index'), 
    ]