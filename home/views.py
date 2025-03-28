from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'education/index.html')



def services(request):
    return render(request, 'education/services.html') 



def teacher(request):
    return render(request, 'education/teacher.html') 


def about(request):
    return render(request, 'education/about.html') 


def pricing(request):
    return render(request, 'education/pricing.html') 



def contact(request):
    return render(request, 'education/contact.html') 