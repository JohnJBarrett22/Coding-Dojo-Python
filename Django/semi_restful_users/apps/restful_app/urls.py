from django.urls import path
from . import views

urlpatterns = [
    path('users', views.index),
    path('users/create', views.create),
    path('users/new', views.new),
    path('users/<int:id>', views.show),
    path('users/<int:id>/edit', views.edit),
    path('users/<int:id>/destroy', views.destroy),
    path('users/update', views.update)
]