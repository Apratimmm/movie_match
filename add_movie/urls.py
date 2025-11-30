
from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('',v.home,name='add_movie'),
    path('search/',v.search,name='search'),
    path('actually_add/',v.add_movie,name='actually_add'),
    path('delete_movie/',v.delete_movie,name='delete_movie'),
]
