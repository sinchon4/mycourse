from django.shortcuts import render
from course.models import *

# Create your views here.


def home(request):
    return render(request,'home.html')
