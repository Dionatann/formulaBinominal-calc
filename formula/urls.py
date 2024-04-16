from django.urls import path
from . import views

urlpatterns = [
    path('formula/', views.binomial_calc, name='binomial_calc'),
]
