from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
# Create your views here.

from meetings.models import Meeting

def welcome(request):
    return HttpResponse("Welcome to meeting planner!")

def date(request):
    return HttpResponse("this page was served at" + str(datetime.now()))

def about(request):
    return HttpResponse("I am Nauman khan & I am a Python Django Developer")