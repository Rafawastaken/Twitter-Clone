from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Tweet

# Home view
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h2>Hello</h2>")

# Tweet detail view
def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    try: # Try to find tweet by id
        tweet = Tweet.objects.get(id = tweet_id)
    except: # If tweet not found/doesnt exist
        raise Http404 # Raise 404 not found
    
    return HttpResponse(f"Tweet id: {tweet.id}: {tweet.content}")

