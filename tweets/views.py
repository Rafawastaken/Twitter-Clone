from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse

from .models import Tweet

# Home view: Landing page
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return render(request, "pages/home.html", context = {})

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