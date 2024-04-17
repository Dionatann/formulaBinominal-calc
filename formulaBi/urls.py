from formula import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.binomial_calc, name='binomial_calc'),
]
