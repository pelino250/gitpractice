from django.urls import path
from . import views

urlpatterns = [
    path('custom/', views.custom_view, name='custom_view'),
]

