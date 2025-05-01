from django.forms import ModelForm
from .models import New, Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
