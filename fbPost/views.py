from django.shortcuts import render,redirect
from pyfacebook import GraphAPI
from django.http import HttpResponse,HttpResponseRedirect
from requests import get
from social_django.models import UserSocialAuth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def fbAuthenticate(response):
    id = '4529360643763975'
    secret = 'c0a34b558471881021117ba6f666f024'

    api = GraphAPI(app_id=id, app_secret=secret, oauth_flow=True)
    link = api.get_authorization_url()[0]
    get(link)
    #print(get(link))
    #api = GraphAPI('4529360643763975|B3vJWwDbQibol1pbj1Ild5RkcsE')
    #a_t = api.get_authorization_url()
    #print(a_t)
    #api.exchange_user_access_token(response='http://localhost:8000/')
    #api.exchange_user_access_token(response="google.com")
    #get('https://www.google.com')
    return HttpResponseRedirect(link)
    #return redirect('contentcreation')

@csrf_exempt
def postAuth(response):
    #response.exchange_user_access_token(response="/")
    #UserSocialAuth.
    #return HttpResponse(response.exchange_user_access_token(response="/"))
    #print(response.)
    return redirect('contentcreation')