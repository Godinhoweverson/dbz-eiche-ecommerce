from .models import Comment
from django import forms
from allauth.account.forms import SignupForm
from django.core.exceptions import ValidationError

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class EditCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)  

    def __init__(self, *args, **kwargs):
        super(EditCommentForm, self).__init__(*args, **kwargs)
        self.fields['text'].widget = forms.Textarea(attrs={'rows': 4})   