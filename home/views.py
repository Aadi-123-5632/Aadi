from django.shortcuts import render,HttpResponse
from home.models import Contact
from django.contrib import messages
def index(request):
    context = {
        'variable':"this is sent"
    }
    return render(request , "index.html")
def about(request):
    return render(request , "about.html")  
def services(request):
    return render(request , "services.html") 
def contact(request):
    if request.method =="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        Phone=request.POST.get('Phone')
        desc=request.POST.get('desc')
        contact=Contact(name=name , email=email ,phone=Phone ,desc=desc)
        contact.save()
        messages.success(request,"Your message has been sent")
    return render(request , "contact.html") 
def Ourvision(request):
    return render(request , "Our vision.html") 
# Create your views here.
