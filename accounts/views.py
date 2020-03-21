from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        #sign user up
        if request.POST['password1'] == request.POST['password2']: #password is a  match
            try:
                #user is in the database
                user = User.objects.get(username=request.POST['username']) 
                return render(request, 'accounts/signup.html', {'error': 'username is taken'})
            except User.DoesNotExist: 
                #user does not exist create one
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('home')
        else:
            #error password must match
            return render(request, 'accounts/signup.html', {'error': 'password must match'})
    else:
        #return user back to the same page
        return render(request, 'accounts/signup.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username and password does not match'})
    else:
        return render(request, 'accounts/login.html')
