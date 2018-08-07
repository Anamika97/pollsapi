from django import forms
from django.contrib.auth.models import User

from .models import Poll, Choice, Vote


class PollForm(forms.ModelForm):

    class Meta:
        model = Poll
        fields = ['question']


class ChoiceForm(forms.ModelForm):

    class Meta:
        model = Choice
        fields = '__all__'


class VoteForm(forms.ModelForm):

    class Meta:
        model = Vote
        fields = ['poll', 'choice']
        

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']