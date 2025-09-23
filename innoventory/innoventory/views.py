from django.shortcuts import render
from django.db import connection
from django.db.utils import OperationalError
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            db_status = True
    except OperationalError:
        db_status = False

    return render(request, 'innoventory/home.html', {'db_status': db_status})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            form = UserCreationForm()
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = UserCreationForm()

    return render(request, 'users/register.html', {'form': form})
