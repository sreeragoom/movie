from django.shortcuts import render

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .forms import UserProfileForm



# Create your views here.

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username taken")
                return redirect('user_app:register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email taken")
                return redirect('user_app:register')
            else:
                user = User.objects.create_user(username=username, password=password, first_name=firstname,
                                                last_name=lastname, email=email)
                user.save()
                return redirect('user_app:message')
        else:
            messages.info(request, "password not matching")
            return redirect('user_app:register')

        return redirect('/')

    return render(request, 'registration.html')

def message(request):
    return render(request,'message_box.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid detail')
            return redirect('user_app:login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def profile(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        email = request.POST['email']
        user = User.objects.filter(username=username, first_name=firstname,
                                   last_name=lastname, email=email)
    return  render(request,'profile.html',)



def edit_profile(request):
    if request.method == 'POST':
        user_form = UserProfileForm(request.POST, instance=request.user)
        if user_form.is_valid() :
            user_form.save()

            return redirect('user_app:profile')  # Redirect to the user profile page after editing

    else:
        user_form = UserProfileForm(instance=request.user)

    return render(request, 'profile_edit.html', {'user_form': user_form})

