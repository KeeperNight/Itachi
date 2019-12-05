from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from user.forms import LoginForm
from user.forms import SignupForm
from django.contrib import messages
import bcrypt
from user.models import User


def user_home(request):

    return render(request,'user/home.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password').encode("utf-8")
            u=User.objects.get(username=username)
            if bcrypt.checkpw(password,u.password):
                return redirect('user_home')
                messages.success(request,f'Login Successful !')
            else:
                messages.error(request, f'password incorrect ','warning')
    else:
        form = LoginForm()
    return render(request, 'user/user_login.html',{'form':form})

def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            fname = form.cleaned_data.get('fname')
            lname = form.cleaned_data.get('lname')
            password = form.cleaned_data.get('password').encode("utf-8")
            conf_password = form.cleaned_data.get('confirm_password').encode("utf-8")
            if password == conf_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request,f'Username exists')
                    return redirect('user_signup')
                else:
                    hashed_password = bcrypt.hashpw(password,bcrypt.gensalt(14))
                    print(hashed_password)
                    #create user with create and assigning form values to model
                    u=User.objects.create(username=username,fname=fname,lname=lname,password=hashed_password)
                    #saving the data to database and committing it
                    u.save()
                    #after save we redirect user to home and render books favourited by user
                    return redirect('user_home')
                    messages.success(request, f'Account created for { username}!')
            else:
                messages.error(request, f'passwords mismatch','warning')
    else:
        form = SignupForm()
    return render(request,'user/user_signup.html',{'form':form})

def update_progress(request):
    return render(request,'user/update_progress.html')

def user_account(request):
    return render(request,'user/user_account.html')
