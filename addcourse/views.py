from django.shortcuts import render
from .models import AddCourse

def addcourse(request):
    if request.method=="POST":
        user = request.POST['id']
        course_name = request.POST['course-name']
        instructor_name = request.POST['instructor-name']
        price_unit = request.POST['price_unit']
        price = request.POST['price']
        category = request.POST['category']
        course_mode = request.POST['course-mode']
        course_url = request.POST['course-url']
        duration = request.POST['duration']
        prerequistes = request.POST['prerequistes']
        description = request.POST['decription']

        add = AddCourse(user_id=user,course_name=course_name,instructor_name=instructor_name,price_unit=price_unit,price=price,category=category,course_mode=course_mode,course_url=course_url,duration=duration,prerequistes=prerequistes,description=description)
        add.save()

    return render(request,'addcourse.html')
