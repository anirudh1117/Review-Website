from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import AddCourseForm
from .models import AddCourse

@login_required
def addcourse(request):
    if request.method=="POST" and request.user.is_authenticated:
        form = AddCourseForm(request.POST)
        print('user ',request.user)
        if form.is_valid():
            form.user_id=request.user
            form.save()
            return render(request,'home.html')
        else:
            print('error')
    
    form = AddCourseForm()
    context={
        'form':form
    }

    return render(request,'addcourse.html',context)
