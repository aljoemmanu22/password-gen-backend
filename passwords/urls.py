from django.urls import path
from .views import generate_password

urlpatterns = [
    path('generate/', generate_password, name='generate_password'),
]
