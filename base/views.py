from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return HttpResponse("This is the homepage")

def room(request):
    return HttpResponse("this is a room")