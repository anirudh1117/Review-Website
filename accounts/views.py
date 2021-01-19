from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from .forms import RegistrationForm,LoginForm

# Create your views here.
def register(request):
    if request.method=='POST':
        print('here')
        form = RegistrationForm(request.POST)
        if form.is_valid():
            name = request.POST["name"]
            email = request.POST["email"]
            password = request.POST["password"]
            username = request.POST["username"]
            user = User(username=username,email=email,password=password,first_name=name)
            user.save()
            user12 = form.save(commit=False)
            user12.user_id=user
            user12.save()
            print('done')
        context={
            'form':form
        }
        return render(request,'signup.html',context)

    form = RegistrationForm()
    context={
        'form':form
    }
    return render(request,'signup.html',context)

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:
                print('login done '+request.user.username)
            print('here')
            return redirect('home')
    form  = LoginForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)
"""
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request,'You are succesfully logged out')
        return redirect('index')

def dashboard(request):
    user_accounts = Contact.objects.order_by('-contact_date').filter(user_id=request.user.id)
    context = {
        'account': user_accounts
    }
    return render(request,'accounts/dashboard.html',context)from django.shortcuts import render, redirect
"""