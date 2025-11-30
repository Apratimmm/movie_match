from django.shortcuts import render
from main.db import db
from pprint import pprint

def provide_top10(request, username, template_name):
    top_10s = db['top_10s']
    current_user = top_10s.find_one({'username': username})
    movies = current_user.get('movies', [])
    if not movies or not current_user:
        return render(request, template_name, {'number': 0, 'username': username} )
    else:
        number = len(movies)
        return render(request, template_name, {'movies': movies, 'number': number, 'username': username})


def show(request):
    username= request.session.get('username')
    return provide_top10(request,username,'top_10s/curr_user_top_10.html')