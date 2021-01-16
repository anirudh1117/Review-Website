
from django.shortcuts import render, redirect
from .models import Courses


# Create your views here.
def allcourse(request):
    Allcourse = Courses.objects.order_by('-published_date')
    context ={
        'course':Allcourse
    }
    return render(request, 'allcourse.html',context)


def Home(request):
    
    return render(request,'home.html')



def About(request):
    return render(request,'about.html')

def courseDetail(request , pk):
    course = Courses.objects.filter(id=pk)
    return render(request, 'course_details.html')

    



