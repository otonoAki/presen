from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from social_django.models import UserSocialAuth
from user_auth.models import Userinfo

from project import settings
from requests_oauthlib import OAuth1Session
import json
import re
import os
import requests
import sys, codecs
from django.http.response import HttpResponse

@login_required
def top_page(request):
    user = UserSocialAuth.objects.get(user_id=request.user.id)
    print('access_token:%s' % user.access_token['oauth_token'])
    print('access_token_secret:%s' % user.access_token['oauth_token_secret'])

    request.POST.get('words')
    msg = request.GET.get('words')

    CK = 'lK2fJktqe3zCT1bGgkt5YVltz'
    CS = 'r0PVHw4VhKycbI8IdBT2jPX6wdjSYvC32fRaUGGNfHPKX6Iapr'
    AK = '1159057082521231360-CI8k8ArX0bVJuQqwN7UnlXSvSZTOlQ'
    AS = 'CiJdnjw09XymMj6AAZMNsnHXTV6LifIgHn0cCZz4IrchM'

    url = "https://api.twitter.com/1.1/statuses/update.json"
    params = {"status": msg,"lang": "ja"}
    tw = OAuth1Session(CK,CS,AK,AS)
    req = tw.post(url, params = params)

    url = 'https://api.twitter.com/1.1/statuses/home_timeline.json'
    params = {'count': 1}
    req = tw.get(url, params = params)

    timeline = json.loads(req.text)
        

    for tweet in timeline:
        Text = (tweet['text'])
        User = (tweet['user']['screen_name'])
        Name = (tweet['user']['name'])
        Img = (tweet['user']['profile_image_url'])
        Cri = (tweet['user']['created_at'])
        Flo = (tweet['user']['followers_count'])
        Fri = (tweet['user']['friends_count'])
        Des = (tweet['user']['description'])
        
        user = {'user': user,
                'words': msg,
                'timeline': timeline,
                'Text': Text,
                'User': User,
                'Name': Name,
                'Img': Img,
                'Cri': Cri,
                'Flo': Flo,
                'Des': Des,
                'Fri': Fri,
            }
    

        return render(request,'top.html', user,)