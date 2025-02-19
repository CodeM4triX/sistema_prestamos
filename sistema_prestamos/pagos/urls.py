from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('register_pay/', views.register_pay, name='register_pay')
]