from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('addword', views.addword),
    path('clear', views.clear)
]
