from django.shortcuts import render
from course.models import *

# Create your views here.
def home(request):
    posts = Post.objects.all() # 메인 페이지
    return render(request, 'main.html')