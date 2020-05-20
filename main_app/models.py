from django.db import models


class TwitterAccount(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=15)
    url = models.URLField()
    most_used_noun = models.CharField(max_length=50)
    most_used_noun_freq = models.IntegerField()
    most_used_adjective = models.CharField(max_length=50)
    most_used_adjective_freq = models.IntegerField()
    most_used_verb = models.CharField(max_length=50)
    most_used_verb_freq = models.IntegerField()
    positivity_score = models.DecimalField(max_digits=4, decimal_places=2)
    last_tweet = models.CharField(max_length=240)

    def __str__(self):
        return self.username


class Tweet(models.Model):
    text = models.CharField(max_length=240)
    username = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE)
    likes = models.IntegerField()
    retweets = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return self.text
