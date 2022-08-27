
import django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
#from mylog.models import Mylog
#from .models import Tactic,Notice
#from join.models import Team
from django.utils import timezone
#from .forms import TacticModelForm,NoticeModelForm
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post, HashTag

#@require_POST
@login_required(login_url='/login/')
def like(request, course_pk):
    if request.user.is_authenticated: 
        course = get_object_or_404(Post, pk=course_pk)

        if course.like_users.filter(pk=request.user.pk).exists(): 
           course.like_users.remove(request.user) 
           course.like_count-=1
           course.save()
        else:
            course.like_users.add(request.user)
            course.like_count+=1
            course.save()
        return redirect('detail',course_pk) 
    return redirect('detail',course_pk)

def CG_filter(request):
    category  = request.GET.get('category', '')
    posts = Post.objects.filter(category = category)
    for post in posts:
        category = post.get_category_display()
        break
    return render(request, 'mapo.html', {'posts': posts, 'category': category})

def LC_filter(request):
    location  = request.GET.get('location', '')
    post = Post.objects.filter(location = location)
    return render(request, 'detail.html', {'post': post})

def course_list(request):
    posts = Post.objects.all() # 메인 페이지
    return render(request, 'course_list.html',{'posts':posts})


def detail(request, post_pk): # 상세 페이지
    post = get_object_or_404(Post, pk=post_pk)
    hashtag = post.hashtag.all()
    return render(request, 'detail.html', {'post': post, 'hashtags':hashtag})

@login_required(login_url='/login/')
def write(request):
    if request.method=='POST' or request.method=='FILES': #파일을 업로드를 요청하거나 post요청을 보낸 경우
        form =PostForm(request.POST, request.FILES) #modelform을 이용한 객체 form은 자체적으로 save method를 가짐.
        #그래서 form.save()가 가능함. medelform을 이용한 객체는 .save()를 지니고 있으므로.
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.user = request.user 
            unfinished.save()
            #new_post = form.save() 
            #new_post.save()
            hashtags = request.POST['hashtags']
            hashtag = hashtags.split(", ")
            for tag in hashtag:
                new_hashtag=HashTag.objects.get_or_create(hashtag = tag)
                #new_post.hashtag.add(new_hashtag[0])
                unfinished.hashtag.add(new_hashtag[0])
            return redirect('home')
    else:
        form=PostForm()
    return render(request, 'write.html', {'form':form})
    #위는 render을 통해서 두번째 인자의 페이지에 (view.py 내의 data를 보내주고 싶을 때) 마지막에 딕셔너리로 해당 data를 보내주는 거다.

def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user=request.user
            comment.save()
            return redirect('detail', post_id)
    
    else:
        form = CommentForm()
    
    return render(request, 'post.html', {'form':form})

# 검색 페이지 (category, location)
