import os.path

from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'caption', 'photo', 'publish']
        widgets = {
            'caption' : forms.Textarea
        }

    def clean_photo(self):
        photo = self.cleaned_data.get('photo')
        if photo:
            split_name = os.path.splitext(photo.name)[-1].lower()
            if split_name not in ('.png', '.jpg'):
                raise forms.ValidationError("You must upload to Photo")
        return photo

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']
        widgets = {
            'message' : forms.Textarea(attrs={'rows' : 3})
        }