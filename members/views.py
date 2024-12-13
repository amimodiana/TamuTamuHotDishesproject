from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import render, redirect


# Create your views here.
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request,'invalid logins. Try again ...')
            return redirect('login_user')
    else:
        return render(request, 'login.html', {})
def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data['username']
            password= form.cleaned_data['password1']
            user =authenticate(username=username, password=password)
            login(request, user)
            messages.success(request,'Registration successful☺️; welcome to TamuTamuHotDishes')
            return redirect('login_user')
        else:
            messages.success(request,'something went wrong.... try again😔')

            return redirect('signup')

    else:
        form = UserCreationForm()

        return render(request,'Register_user.html',{'form' : form})
