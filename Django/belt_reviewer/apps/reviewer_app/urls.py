from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books', views.books),
    path('add', views.add),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('addbook', views.addbook),
    path('addreview', views.addreview),
    path('books/<int:id>', views.bookdetails),
    path('users/<int:id>', views.userdetails)
]