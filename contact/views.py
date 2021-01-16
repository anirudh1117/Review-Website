from django.shortcuts import render
from .models import Contact_table

def Contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        contact = Contact_table(name=name,email=email,subject=subject,message=message)
        contact.save()
        #send_mail(subject= subject,message= message,from_email=settings.DEFAULT_FROM_EMAIL,recipient_list = [email],fail_silently  = True,)
        return render(request,'home.html')
    return render(request,'contact.html',{})
