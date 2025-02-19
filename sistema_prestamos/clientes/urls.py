from django.urls import path
from . import views

urlpatterns = [
    path('clients/', views.clients, name='clients'),
    path('register_clients/', views.register_clients, name='register_clients')
]