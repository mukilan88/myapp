from django.urls import path

from . import views

urlpatterns = [
    path('home/',views.home, name='home'),
    path('uin',views.uin, name='uin'),
    path('', views.index, name='index'),
    path('bot', views.bot, name='bot')
]