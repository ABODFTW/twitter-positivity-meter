from twitter_positvity_meter.settings import config

# Configure Django App for Heroku.
import django_heroku

config.DEBUG = False

django_heroku.settings(locals())
