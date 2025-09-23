from django.urls import path
from .views import register  # import register view from this app

urlpatterns = [
    path('register/', register, name='register'),
]
