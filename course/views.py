from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostForm
from .models import Post


def CG_filter(request):
    category  = request.GET.get('category', '')
    posts = Post.objects.filter(category = category)
    return render(request, 'detail.html', {'posts': posts})

def LC_filter(request):
    location  = request.GET.get('location', '')
    post = Post.objects.filter(location = location)
    return render(request, 'detail.html', {'post': post})




def detail(request, pk): # 상세 페이지
    posts = Post.objects.get(id = pk)
    return render(request, 'detail.html', {'posts': posts})

def write(request):
    if request.method=='POST' or request.method=='FILES': #파일을 업로드를 요청하거나 post요청을 보낸 경우
        form =(request.POST, request.FILES) #modelform을 이용한 객체 form은 자체적으로 save method를 가짐.
        #그래서 form.save()가 가능함. medelform을 이용한 객체는 .save()를 지니고 있으므로.
        if form.is_valid():
            new_post = form.save() 
            new_post.save()
            hashtags = request.POST['hashtags']
            hashtag = hashtags.split(", ")
            for tag in hashtag:
                new_hashtag=HashTag.objects.get_or_create(hashtag = tag)
                new_post.hashtag.add(new_hashtag[0])
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
            comment.save()
            return redirect('detail', post_id)
    
    else:
        form = CommentForm()
    
    return render(request, 'post.html', {'form':form})

# 검색 페이지 (category, location)
