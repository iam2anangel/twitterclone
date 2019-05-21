from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from twitterclone.tweet.models import Tweet
from twitterclone.twitteruser.models import TwitterUser


@login_required()
def home_view(request):
    html = "home.html"
    tweets = Tweet.objects.filter().order_by("-date")
    tweets_of_followings = Tweet.objects.filter()
    return render(request, html, {"tweets": tweets})