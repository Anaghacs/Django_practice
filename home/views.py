from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Home page")

def about(request):
    return render(request, 'about.html')
    # return HttpResponse("About page")

def booking(request):
    return render(request,'booking.html')
    # return HttpResponse("Booking page")

def doctors(request):
    return render(request,'doctors.html')
    # return HttpResponse("Doctors page")