from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new),
    path('create', views.create),
    path('<num>', views.show),
    path('<num>/edit', views.edit),
    path('<num>/destroy', views.destroy)
]