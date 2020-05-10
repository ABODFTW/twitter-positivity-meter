from django.db import models


# Create your models here.
class TwitterAccount(models.Model):
    account_name = models.CharField(max_length=50)
    account_username = models.CharField(max_length=15)
    account_url = models.URLField()
    most_used_word = models.CharField(max_length=50)
    most_used_word_frequency = models.IntegerField()
    positive_to_negative_ratio = models.DecimalField(max_digits=2, decimal_places=2)

    def __str__(self):
        return self.account_name


class Tweet(models.Model):
    text = models.CharField(max_length=240)
    username = models.ForeignKey(TwitterAccount, on_delete=models.CASCADE)
    likes = models.IntegerField()
    retweets = models.IntegerField()
    date = models.DateTimeField()
