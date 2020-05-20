from django.contrib import admin
from main_app.models import TwitterAccount, Tweet

# Register your models here.
admin.site.register(TwitterAccount)
admin.site.register(Tweet)
