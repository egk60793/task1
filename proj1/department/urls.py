from django.urls import path
from . import views

urlpatterns = [
    path('', views.contacts, name='contacts'),
    path('get_users/', views.get_users)
    ]