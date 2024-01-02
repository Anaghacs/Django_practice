from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):

    # variable values passing by the html page
    # person={
    #     'name':'Anagha',
    #     'age':23,
    #     'place':'Thrissur'
    # }

    numbers={
         'num1':10     
     }
    return render(request,'home.html',numbers)
    # return HttpResponse("Home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About page")

def booking(request):
    return render(request,'booking.html')
    # return HttpResponse("Booking page")

def doctors(request):
    return render(request,'doctors.html')
    # return HttpResponse("Doctors page")