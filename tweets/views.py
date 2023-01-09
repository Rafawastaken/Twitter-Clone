from django.shortcuts import render
from django.http import HttpResponse

# Routes

# Home view
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    return HttpResponse("<h2>Hello</h2>")

# Tweet detail view
def tweet_detail_view(request, tweet_id,  *args, **kwargs):
    return HttpResponse(f"Tweet_detail_view: {tweet_id}")