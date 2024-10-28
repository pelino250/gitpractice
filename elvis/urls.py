from django.urls import path
from .views import BikeListView

app_name = 'elvis'

urlpatterns = [
    path('', BikeListView.as_view(), name='bike-list'),
]