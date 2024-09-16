from django.urls import path
from telebot.views import tguser, load_tgusers

urlpatterns = [
    path('', tguser, name='tgusers'),
    path('view/', load_tgusers, name='view_tgusers')
]
