from django.urls import path
from . import views

urlpatterns = [
    path('loans/', views.loans, name='loans'),
    path('register_loan/', views.register_loan, name='register_loan')
]