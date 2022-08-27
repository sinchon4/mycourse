
from django.contrib import admin
from django.urls import path
from accounts import views as account
from home import views as home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.home, name='home'),
    path('login/',account.login, name='login'),
    path('logout/', account.logout, name='logout'),
    path('signup/', account.signup, name='signup')
]

