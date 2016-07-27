from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, note

class noteForm(forms.ModelForm):
    author = forms.CharField(required=False)
    book_title = forms.CharField(required=False)
    page = forms.IntegerField()
    chapter = forms.CharField(max_length = 100)
    content = forms.CharField(max_length = 200, widget=forms.Textarea)
    class Meta:
        model = note
        fields = ('chapter', 'page', 'content',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)