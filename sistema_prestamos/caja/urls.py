from django.urls import path
from . import views

urlpatterns = [
    path('caja/', views.caja, name='caja'),
    path('agregar_dinero_caja/', views.agregar_dinero_caja, name='agregar_dinero_caja')
]