from django import forms


class TweetForm(forms.Form):
    tweet = forms.CharField(label='Write your tweet', max_length=144)
