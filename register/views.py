from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from main.db import db

def register(request):
    return render(request,'register.html')

def check_username(request):
    username=request.GET.get('username')
    user_table=db['user']
    if (user_table.find_one({'username':username})):
        return JsonResponse({'exist_username':username})
    else:
        return JsonResponse({'unique_username':username})

class user:
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def todict(self):
        return {
            'username': self.username,
            'password': self.password,
        }

def add(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_table = db['user']
        newuser = user(username,password)
        user_table.insert_one(newuser.todict())
        top_10s = db['top_10s']
        top_10s.insert_one({'username': username, 'movies': []})
        user_vectors = db['user_vectors']
        user_vectors.insert_one({'username': username, 'vector': []})
    return redirect('login_page')