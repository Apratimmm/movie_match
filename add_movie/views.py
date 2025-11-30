from django.contrib.admin.templatetags.admin_list import results
from django.http import JsonResponse
from django.shortcuts import render, redirect
import requests
from pprint import pprint
from .models import genre_maps
from user_info.views import arranged
from find_match.views import find_vector

from pymongo.errors import DuplicateKeyError

from main.db import db
import json

def home(request):
    return render(request,'add_movie.html')

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlOGJjMjcwMzEwYmNkYmRjOGU5NGNiYWIxNWM5NzFjZCIsIm5iZiI6MTc2MjY3NTU5Mi43MjQsInN1YiI6IjY5MTA0Yjg4OTkxM2QzYzRmOTg3NGQxZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.U-gSlo1XEJRrL4QmDMQADCtbsCrK5r_1_rCGcrSqnZU"
}

def maps(genre_ids):

    genres=[]
    for g_ids in genre_ids:
            genre= genre_maps[g_ids]
            if genre:
                genres.append(genre)
    return genres

def search(request):
    movie_name= request.GET.get('moviename')
    params={
            "query":movie_name,
            "language":"en-US",
    }

    url= "https://api.themoviedb.org/3/search/movie"
    response = requests.get(url, headers=headers, params=params, timeout=5)
    moviess=response.json()
    movies=moviess.get('results',[])
    if movies == []:
        return render(request,'add_movie.html',{'message':'No movies found'})
    movie_details = []
    for movie in movies:
        details={
            "id": int(movie['id']),
            "title" : movie['original_title'],
            "release_date": movie['release_date'],
            "original_language": movie['original_language'],
            "popularity": movie['popularity'],
            "overview": movie['overview'],
            "picture_url": movie['poster_path'],
            "genres": maps(movie.get('genre_ids',[])),
        }
        movie_details.append(details)
    return render(request,'add_movie.html',{'movies':movie_details,'user_input':movie_name})

def add_movie(request):
    movie_details= json.loads(request.body)
    username= request.session.get('username')
    top_10s= db['top_10s']

    data= top_10s.find_one({'username':username})
    if (data):
        if (len(data['movies'])==10):
            return JsonResponse({'message':'enough'})

    result = top_10s.update_one(
            {"username": username},
            {"$addToSet": {"movies": movie_details}},
            upsert=True
            )

    if result.modified_count > 0:
        return JsonResponse({'message': 'yes'})
    else:
        return JsonResponse({'message': 'no'})

def delete_movie(request):
    movie_id= request.GET.get('movieId')
    username = request.session.get('username')
    top_10s = db['top_10s']

    top_10s.update_one(
        {"username":username},
        {"$pull":{"movies":{ "id":int(movie_id) }}},)

    updatedtop_10s= db['top_10s']
    newtop_10s = updatedtop_10s.find_one({"username":username})
    movies = newtop_10s.get('movies',[])
    if not movies:
        return render(request, 'top_10s/curr_user_top_10.html',{'message':'empty'})
    else:
        number = len(movies)
        return render(request, 'top_10s/curr_user_top_10.html',{'movies':movies, 'number':number})


