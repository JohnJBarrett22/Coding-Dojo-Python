from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('register', views.register),
    path('login', views.login),
    path('wall', views.wall),
    path('post', views.post),
    path('comment', views.comment),
    path('logout', views.logout),
    path('delmsg/<int:id>', views.delmsg),
    path('delcom/<int:id>', views.delcom)
]