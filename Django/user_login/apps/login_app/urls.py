from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('all.json', views.all_json),
    path('all.html', views.all_html),
    path('find', views.find),
    path('create', views.find)
]