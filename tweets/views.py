# Python
import random

# Django
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, JsonResponse, HttpResponseRedirect
from django.utils.http import is_safe_url

# Local
from .models import Tweet
from .forms import TweetForm


# Configs
ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Home view: Landing page
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context = {})


# Tweet List view
def tweet_list_view(request, *args, **kwargs):
    tweets = Tweet.objects.all()
    
    # Add all tweets to an array with tweets object
    tweet_list = [tweet.serialize() for tweet in tweets]
    
    data = {
        "isUser": False,
        "response": tweet_list
    }

    return JsonResponse(data )


# Tweet detail view
def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    data = { "id":tweet_id }
    status = 200 # Initial status OK

    try: # Try tp find tweet by id
        tweet = Tweet.objects.get(id = tweet_id)
        data['content'] = tweet.content # Append content resp
    except: # Tweet not found
        data['message'] = "Not found"
        status = 404 # Change status NOT FOUND

    return JsonResponse(data, status = status) # json dumps application/json


# create tweet form
def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get('next') or None

    if form.is_valid():
        obj = form.save(commit = False)
        obj.save()

        if request.is_ajax(): return JsonResponse(obj.serialize(), status = 201) # Created items
        form = TweetForm()
        
    if form.errors:
        if request.is_ajax():
            return JsonResponse(form.errors, status = 400) # 400 error
    return render(request, 'components/form.html', context = {'form': form})