from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        c_password = request.POST['c_password']

        details = User.objects.create_user(username, password, c_password)

        details.save()
        messages.success(request, 'Your account has been created Successfully')
        return redirect('signin')
    return render(request, 'register.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            print(" signin")
            print(user)
            print(user.id)
            return render(request, 'user_registration.html', {'user': user})
        else:
            messages.error(request, 'Wrong Credentials')
            return render(request, 'login.html')

    return render(request, 'login.html')


def user_registration(request):
    print("in user reg")
    print(request)

    return render(request, 'user_registration.html')


def logout(request):
    logout()
