from django.contrib import admin
from django.urls import path

# My routes
from tweets.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
    path('tweets/<int:tweet_id>', tweet_detail_view)
]
