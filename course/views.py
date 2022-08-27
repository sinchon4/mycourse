import django
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.models import User
#from mylog.models import Mylog
from .models import Tactic,Notice
#from join.models import Team
from django.utils import timezone
#from .forms import TacticModelForm,NoticeModelForm
from django.contrib.auth.decorators import login_required


#@require_POST
@login_required(login_url='/login/')
def like(request, course_pk):
    if request.user.is_authenticated: #로그인된 요저인 경우.
        course = get_object_or_404(Notice, pk=course_pk)

        if course.like_users.filter(pk=request.user.pk).exists(): #해당 게시글을 좋아요한 사람중에 pk가 현재 유저의 pk랑 같은 것이 존재하는지 하지 않는지를 판단한다
           course.like_users.remove(request.user) #여기 실행되나?
           course.like_count-=1
           course.save()
            #notice.check_users.remove(request.user)
        else:
            course.like_users.add(request.user) #여기 실행되나?
            course.like_count+=1
            course.save()
        return redirect('myteam_notice') # return redirect('articles:index')
    return redirect('myteam_notice') #return redirect('accouts:login')