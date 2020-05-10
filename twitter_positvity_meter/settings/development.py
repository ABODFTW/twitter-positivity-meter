from twitter_positvity_meter.settings import config
import os

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(config.BASE_DIR, "db.sqlite3"),
    }
}
