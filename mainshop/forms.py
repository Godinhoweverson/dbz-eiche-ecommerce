from .models import Comment
from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


        