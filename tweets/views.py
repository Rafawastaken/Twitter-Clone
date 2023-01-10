from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet


# * REST API * -> Returns JSON data to be fed to frontend

# Home view
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h2>Hello</h2>")

# Tweet detail view
def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    data = {
        "id":tweet_id
    }

    status = 200 # Initial status OK

    try: # Try tp find tweet by id
        tweet = Tweet.objects.get(id = tweet_id)
        data['content'] = tweet.content # Append content resp
    except: # Tweet not found
        data['message'] = "Not found"
        status = 404 # Change status NOT FOUND
        raise Http404

    return JsonResponse(data, status = status) # json dumps application/json