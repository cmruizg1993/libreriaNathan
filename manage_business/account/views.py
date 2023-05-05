
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
# from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, RegisterForm
def registrate(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():          
            form.save()
            messages.success(request, 'Your account has been created successfully!')

        else:
            for field_name, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field_name}: {error}')
            messages.error(request, 'There was an error creating your account. Please try again.')
    else:
        form = RegisterForm()

    return render(request, 'registration/registrate.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse_lazy('home'))
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm(request=request)
    return render(request, 'registration/login.html', {'form': form})