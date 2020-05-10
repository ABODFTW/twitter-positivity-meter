from django import forms

from main_app.models import TwitterAccount


class TwitterSearchForm(forms.ModelForm):
    class Meta:
        model = TwitterAccount
        fields = ("account_username",)
