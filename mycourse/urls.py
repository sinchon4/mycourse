from django.contrib import admin
from django.urls import path
from course import views as cs_views
from home import views as hm_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hm_views.home, name ="home"),
    path('list_lc', cs_views.LC_filter, name = "lc_filter"),
    path('list_cg', cs_views.CG_filter, name="cg_filter"),
]
