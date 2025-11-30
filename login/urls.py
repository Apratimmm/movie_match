
from django.contrib import admin
from django.urls import path, include
from . import views as v

urlpatterns = [
    path('', v.login, name='login_page'),
    path('actual_login/',v.actual_login, name='actual_login'),
]
