from twitter_positvity_meter.settings.config import *
import django_heroku

# Configure Django App for Heroku.

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}


django_heroku.settings(locals())
