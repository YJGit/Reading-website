from django import forms
from django.contrib.auth.models import User
from .models import UserProfile, note

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'address')

class noteForm(forms.ModelForm):
    time = forms.CharField(required=False)
    author = forms.CharField(required=False)
    book_title = forms.CharField(required=False)
    page = forms.IntegerField(required=True)
    chapter = forms.CharField(max_length = 100, required=True)
    content = forms.CharField(max_length = 1000, widget=forms.Textarea, required=True)
    class Meta:
        model = note
        fields = ('chapter', 'page', 'content',)