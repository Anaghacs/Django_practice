from django.shortcuts import render
from django.http import HttpResponse
from .models import App1
# Create your views here.

def display(request):
    # obj=App1(name='anagha')
    # obj.save()
    data=App1.objects.all()
    for i in data:
        print(i.name)
    return HttpResponse('welcome')

