from django.urls import include, path
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('Cecilia_todos/', include('Cecilia_todos.urls'))
    # Include other paths for your app here
]