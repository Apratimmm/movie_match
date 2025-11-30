
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('login.urls')),
    path('register/',include('register.urls')),
    path('add_movie/',include('add_movie.urls')),
    path('top_10/',include('top_10.urls')),
    path('home/',include('home.urls')),
    path('user_info/',include('user_info.urls')),
    path('show_users/', include('show_users.urls')),
    path('find_match/',include('find_match.urls')),
 ]
