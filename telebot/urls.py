from django.urls import path
from telebot.views import tguser

urlpatterns = [
    path('', tguser, name='tgusers')
]
