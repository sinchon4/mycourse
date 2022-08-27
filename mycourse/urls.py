
from django.contrib import admin
from django.urls import path
from accounts import views as account
from home import views as home
from course import views as cs_views
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('login/',account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('signup/', account.signup, name='signup'),
    path('list_lc', cs_views.LC_filter, name = "lc_filter"),
    path('list_cg', cs_views.CG_filter, name="cg_filter"),
    path('post/',cs_views.write,name='write'),
    path('detail/<int:post_pk>/',cs_views.detail, name='detail'),
    path('like/<int:course_pk>/',cs_views.like,name='like' ),
    path('course_list/',cs_views.course_list,name='course_list'), #작성한 코스들이 보이는 페이지
]


