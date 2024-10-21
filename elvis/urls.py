from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_claude, name='hello_elvis'),
]