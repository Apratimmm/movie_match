from pydoc import doc

from django.shortcuts import render
from  main.db import db
from user_info.views import arranged
from add_movie.models import genre_maps
import numpy as np
from pprint import pprint
from top_10.views import provide_top10

def turn_into_set():
    genres = set()
    for key, value in genre_maps.items():
        genres.add(value)
    return sorted(list(genres))

def find_vector(username):
    base_vector = ['Action', 'Adventure', 'Animation', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Family', 'Fantasy', 'History', 'Horror', 'Music', 'Mystery', 'Romance', 'Science Fiction', 'TV Movie', 'Thriller', 'War', 'Western']

    top_10s = db['top_10s']
    user = top_10s.find_one({'username': username})
    movies = user.get('movies', [])
    demo_vector = arranged(movies)[0]
    user_vector = []
    for genre in base_vector:
        if genre in demo_vector:
            user_vector.append(demo_vector[genre])
        else:
            user_vector.append(0)
    return user_vector

def show_vector(request):
    username = request.session.get('username')
    user_vector = find_vector(username)
    request.session['user_vector'] = user_vector
    return render(request, 'match/find_match.html', {'user_vector': user_vector})

def cosine_sim(a, b):
    return (np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

def similairty_score(a , b):
    a = np.array(a)
    b = np.array(b)
    return round(cosine_sim(a, b)*100,2)

def show_results(request):
    curr_user = request.session.get('username')
    curr_user_vector = request.session.get('user_vector')
    top_10s = db['top_10s']
    users = db['user']
    user_and_vector = {}
    for doc in users.find():
        user = doc["username"]
        if user != curr_user:
            user_and_vector[user] = find_vector(user)
    final_score = {}
    for name, other_user_vector in user_and_vector.items():
        final_score[name]= similairty_score(curr_user_vector,other_user_vector)
    pprint(final_score)

    sorted_final_score = sorted(
        final_score.items(), 
        key=lambda item: (item[1] if not np.isnan(item[1]) else -1), 
        reverse=True
    )
    pprint(sorted_final_score)
    return render(request, 'match/found_match.html', {'final_score': sorted_final_score})

def show_top_10s(request):
    username = request.GET.get('username')
    return provide_top10(request, username, 'match/top_10s.html')
