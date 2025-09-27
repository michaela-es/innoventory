from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    # path('dashboard/', dashboard_redirect, name='dashboard'),
    # path('admin-dashboard/', admin_dashboard, name='admin_dashboard'),
    # path('staff-dashboard/', staff_dashboard, name='staff_dashboard'),
]
