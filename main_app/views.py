from django.shortcuts import render, HttpResponse

import GetOldTweets3 as got

# Create your views here.
def index(request):
    return render(request, 'main_app/index.html')

def get_tweets(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        tweet_criteria = got.manager.TweetCriteria().setUsername("realdonaldtrump")\
                                           .setMaxTweets(10)\
                                           .setEmoji("unicode")
        tweets = got.manager.TweetManager.getTweets(tweet_criteria)
        print(tweets)
        return render(request, 'main_app/index.html', {'tweets':tweets})
    else:
        return render(request, 'main_app/index.html')
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = NameForm()

    # return render(request, 'name.html', {'form': form})
