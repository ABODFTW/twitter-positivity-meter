from django.shortcuts import render, redirect
from django.urls.exceptions import NoReverseMatch

import GetOldTweets3 as got

from main_app.tools import ReportDetails


# Create your views here.
def index(request):
    return render(request, "main_app/index.html")


def get_tweets(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        twitter_username = request.POST["twitter-username"]
        try:
            return redirect("account-page", username=twitter_username)
        except NoReverseMatch:
            from django.contrib import messages

            messages.add_message(request, messages.INFO, "Make sure to type username")
            return render(request, "main_app/index.html")
    else:
        return render(request, "main_app/index.html")
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = NameForm()

    # return render(request, 'name.html', {'form': form})


def get_account_details(request, username):
    # Move this logic to Models later
    if request.method == "GET":
        tweet_criteria = (
            got.manager.TweetCriteria()
            .setUsername(username)
            .setMaxTweets(100)
            .setEmoji("unicode")
        )
        tweets = got.manager.TweetManager.getTweets(tweet_criteria)

        report = ReportDetails(tweets)

        context = {
            "tweets": report.tweets,
            "username": username,
            "report_details": {
                "Most used Noun": report.get_most_used_words("NNP"),
                "Most used Adjective": report.get_most_used_words("JJ"),
                "Most used Verb": report.get_most_used_words("VB"),
                "Positivity Score (100 to -100)": report.get_avg_positivity_score(),
            },
        }
        return render(request, "main_app/twitter-account-page.html", context=context)
