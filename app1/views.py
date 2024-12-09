from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.



def index(request):
    return render(request,'index.html')


def services(request):
    return render(request,'services.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')