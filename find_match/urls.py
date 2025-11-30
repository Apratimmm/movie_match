
from django.contrib import admin
from django.urls import path,include
from . import views as v
urlpatterns = [
    path('', v.show_vector , name='find_vector'),
    path('show_results/', v.show_results , name='show_results'),
    path('show_top_10s/',v.show_top_10s , name='show_top_10s'),
 ]
