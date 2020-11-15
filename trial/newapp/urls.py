from django.conf.urls import url,include
from django.urls import path,re_path
from . import views

app_name='newapp'
urlpatterns =\
    [
    path('',views.home,name='home'),
    re_path('^login',views.login_page,name='login_page'),
    re_path('^signup',views.signup,name='signup'),
    re_path('^logout',views.logout_user,name='logout_user'),
    re_path('^main',views.main_page, name='main_page'),
    re_path('^display',views.display_page,name='display_page'),
    re_path('^map',views.map_display,name='map_display'),
    re_path('^profile',views.profile_page,name='profile_page')
    ]