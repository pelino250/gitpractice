from django.urls import path
from . import views

app_name = 'esther'
urlpatterns = [
    path('', views.welcome, name='welcome'),
]
