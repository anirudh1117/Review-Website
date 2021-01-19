from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .forms import RegistrationForm, LoginForm
from django.contrib import auth
from .check_username_or_email import check_username_or_email

# Create your views here.


def register(request):
    if request.method == 'POST':
        print('here')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            username = request.POST["username"]
            user = User(username=username, email=email,
                        password=password, first_name=name)
            user.save()
            user12 = form.save(commit=False)
            user12.user_id = user
            user12.save()
            print('done')
        context = {
            'form': form
        }
        return render(request, 'signup.html', context)

    form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'signup.html', context)


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["email"]
            password = request.POST["password"]
            username=check_username_or_email(username)
            if username:
                user = auth.authenticate(username=username,password=password)
                if user is not None:
                    auth.login(request,user)
                    if request.user.is_authenticated:
                        print("login done ")
                    return redirect('home')
        context ={
                'form': form
            }
        return render(request, 'login.html', context)
    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('home')

"""
def dashboard(request):
    user_accounts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'account': user_accounts
    }
    return render(request,'accounts/dashboard.html',context)from django.shortcuts import render, redirect
"""
