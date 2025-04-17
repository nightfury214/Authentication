from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import UserForm
from .models import User
from .decorators import status_user



def home(request):
    return render(request, 'registration/home.html')

@status_user
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # print(form.is_valid())
        # print("Form errors:", form.errors)  
        if form.is_valid():
            user = form.save()
            # login(request, user)
            # return redirect("successfully")
            return redirect('login')
    else:
        form = UserForm()
        # return HttpResponse("<h2>Failed</h2>")
    return render(request, 'registration/register.html', {'form': form})

@status_user
def login(request):
    users = User.objects.all()
    # User.objects.filter(first_name='nick')

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password = password)
        # return redirect('employee_table')      
        if user is not None:
            # login(request, user) 
            # return redirect('somewhere')
            # return HttpResponse("successfully")
            return redirect('employee_table')
        else:
            # messages.error(request, 'Invalid email or password.')
            return redirect('home')
        # if not email or not password:
        #     messages.error(request, "Please enter both email and password.")
        #     return render(request, 'registration/login.html')
        
    return render(request, 'registration/login.html')