from django.shortcuts import render, redirect
from django.urls.exceptions import NoReverseMatch

from django.contrib import messages

import GetOldTweets3 as got

from main_app.tools import ReportDetails
from main_app.models import TwitterAccount

import requests
import json


# Create your views here.
def index(request):
    return render(request, "main_app/index.html")


def get_account(request):
    # Check if username is in DB
    if request.method == "POST":
        username = request.POST["twitter-username"]
        query = TwitterAccount.objects.filter(username=username)
        if query.exists():

            return redirect("account-page", username=username)
        else:
            # Check if username is valid
            response = requests.get(f"https://www.twitter.com/{username}")
            if response.ok:
                # Add the logic to add the account to the DB
                pass
            else:
                messages.add_message(
                    request,
                    messages.WARNING,
                    "Make sure to enter a valid twitter username",
                )
                return render(request, "main_app/index.html")

    # # if this is a POST request we need to process the form data
    if request.method == "POST":
        twitter_username = request.POST["twitter-username"]
        try:
            return redirect("account-page", username=twitter_username)
        except NoReverseMatch:
            messages.add_message(
                request, messages.WARNING, "Make sure to enter a valid twitter username"
            )
            return render(request, "main_app/index.html")
    else:
        return render(request, "main_app/index.html")


def generate_report(request, username, tweets=100):
    # Move this logic to Models later
    username = username.lower()
    tweets_amount = tweets
    if request.method == "GET":
        # if TwitterAccount.objects.get(account_username=username).exists():
        #     pass
        # else:
        tweet_criteria = (
            got.manager.TweetCriteria()
            .setUsername(username)
            .setMaxTweets(tweets_amount)
            .setEmoji("unicode")
        )
        tweets = got.manager.TweetManager.getTweets(tweet_criteria)

        report = ReportDetails(tweets)
        muw = report.get_most_used_words(
            ["JJ", "JJR", "JJS", "NN", "NNS", "NNP", "NNPS"]
        )
        words = muw[0]
        scores = report.get_positivity_score(words)
        context = {
            "tweets": report.tweets,
            "username": username,
            # "report_details": {"Most used words": "", "Most used words values": "",},
            "MUW": json.dumps(muw),
            "SCORES": json.dumps(scores),
        }
        return render(request, "main_app/twitter-account-page.html", context=context)
