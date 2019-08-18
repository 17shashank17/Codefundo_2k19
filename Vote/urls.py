from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$',views.home,name="home"),
    url(r'^voter/',views.voter,name="voter"),
    url(r'^candidate/',views.candidate,name="candidate"),
    url(r'^feedback/',views.feedback,name="feedback"),
    url(r'^login/',views.login_user,name="login_user"),
    url(r'^logout/',views.logout_user,name="logout_user"),
    url(r'^profile',views.profile,name="profile"),
    url(r'^token',views.save_token,name="save_token"),
]