""" urls file of the SPEECHES app """
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_speeches, name='speeches'),
    path('<speech_id>', views.speech_detail, name='speech_detail')
]