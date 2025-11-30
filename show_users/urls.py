
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('',v.show_other_users, name='show_other_users'),
    path('top_10s/',v.other_top_10s, name='show_other_user_top_10s'),
 ]
