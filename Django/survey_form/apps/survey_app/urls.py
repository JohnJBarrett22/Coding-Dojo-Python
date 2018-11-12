from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('process', views.process),
    path('results', views.results),
    path('goback', views.goback),
    path('delete', views.delete)
]