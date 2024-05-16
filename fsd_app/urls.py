from django.urls import path
from fsd_app import views

urlpatterns = [
    path('home',views.home),
    path('create',views.create),
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('',views.index),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout)
]