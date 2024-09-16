from django.urls import path
from telebot.views import tguser, View_tgusers

urlpatterns = [
    path('', tguser, name='tgusers'),
    path('view/', View_tgusers.as_view(), name='view_tgusers')
]
