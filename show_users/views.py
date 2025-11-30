from pprint import pprint

from django.shortcuts import render
from main.db import db
from top_10.views import provide_top10


def show_other_users(request):
    user= db['user']
    curr_user = request.session.get('username')
    users = user.find({},{'_id':0,'username':1})
    final_users = []
    for u  in users:
        uu = u['username']
        if uu != curr_user:
            final_users.append(uu)
    pprint(final_users)

    pprint('working')
    return render(request, 'other_users.html', {'users':final_users})


def other_top_10s(request):
    username = request.GET.get('username')
    return provide_top10(request, username, 'top_10s/other_user_top_10.html')
