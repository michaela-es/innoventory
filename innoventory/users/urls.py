from django.urls import path
from .views import register, login  # import register view from this app

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
]
