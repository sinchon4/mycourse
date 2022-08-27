from django.shortcuts import render
from .models import Post


def CG_filter(request):
    category  = request.GET.get('category', '')
    posts = Post.objects.filter(category = category)
    return render(request, 'detail.html', {'posts': posts})

def LC_filter(request):
    location  = request.GET.get('location', '')
    post = Post.objects.filter(location = location)
    return render(request, 'detail.html', {'post': post})
