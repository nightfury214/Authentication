from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate ,login as auth_login, get_user_model
from .forms import UserForm
from .decorators import status_user
User = get_user_model()  # This gets your custom user model (accounts.User)

@status_user
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
    return render(request, 'registration/register.html', {'form': form})

@status_user
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # try:
        #     user_obj = User.objects.get(email = email)
        user = authenticate(request, email=email, password = password)
        # except User.DoesNotExist:

            # user = None
        if user is not None:
            auth_login(request, user)
            return redirect('employee_table')
        else:
            return redirect('home')
        
    return render(request, 'registration/login.html')