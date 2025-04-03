from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_livros, name='lista_livros'), 
    path('/api/livros/',views.listar_adcionar, name='listar_adcionar'),
]
