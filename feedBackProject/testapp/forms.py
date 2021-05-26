from django import forms
from django.core import validators

#def starts_with_d(value):
    #if value[0] != 'd':
        #raise forms.ValidationError('must start with d')

def gmail_verification(value):
    if value[len(value)-9:] != '@gmail.com':
        raise forms.ValidationError('must be gmail')


class FeedBackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField(validators=[gmail_verification])
    feedback = forms.CharField(widget=forms.Textarea)

    