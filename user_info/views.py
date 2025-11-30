from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import requests
from pprint import pprint
from main.db import db
import json
from django.shortcuts import render
from collections import OrderedDict, Counter

def show_user_info(request):

    username = request.session.get('username')
    top_10s = db['top_10s']

    user = top_10s.find_one({'username':username})
    movies = user.get('movies', [])
    if not user or not movies:
        return JsonResponse({'message': 'start adding movies into your top_10s'})

    count_genres, number_of_entries = arranged(movies)
    request.session['count_genres'] = count_genres
    final_result = count_to_percentage(number_of_entries , count_genres )
    return render(request, 'user_info.html', {'info':final_result})

def count_to_percentage(number_of_entries, count_genres ):
    final_dic = {}
    for genre in count_genres:
        per = (count_genres[genre] / number_of_entries) * 100
        final_per = round(per, 2)
        final_dic.update({genre: final_per})
    return final_dic

def arranged(movies):
    genres = []

    for movie in movies:
        for genress in movie['genres']:
            genres.append(genress)

    number_of_entries = len(genres)
    count_genres = dict(Counter(genres))
    sorted_count_genres = dict(sorted(count_genres.items(), key=lambda item: item[1], reverse=True))
    return ( sorted_count_genres, number_of_entries )
