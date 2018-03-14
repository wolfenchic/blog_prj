from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'image')

        
class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'content', 'tag', 'image')