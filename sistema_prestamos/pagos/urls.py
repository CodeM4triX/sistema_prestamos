from django.urls import path
from . import views

urlpatterns = [
    path('payments/', views.payments, name='payments'),
    path('register_pay/', views.register_pay, name='register_pay'),  # sin id
    path('register_pay/<int:id>/', views.register_pay, name='register_pay_with_id') # con id
]