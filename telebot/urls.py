from django.urls import path
from telebot.views import Register1

urlpatterns = [
    path('', Register1.as_view(), name='register1')
]
