
from django.contrib import admin
from django.urls import path,include
from . import views as v

urlpatterns = [
    path('', v.show_user_info, name='show_user_info'),
]
