from django.shortcuts import render, redirect
from django.http import HttpResponse
from main.db import db

def login(request):
    return render(request, 'login.html')

def actual_login(request):
    if request.method == "POST":
        username = request.POST.get('username_input')
        password = request.POST.get('password_input')

        usertable=db['user']
        fetched_user= usertable.find_one({'username': username})

        if not (fetched_user):
            return render(request,'login.html',{'error1':password})

        else:
               if  fetched_user['password'] != password:
                   return render(request,'login.html',{'error2':username})

        request.session['username'] = username
        return redirect('home')

    return render(request,'login.html')

