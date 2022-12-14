from socket import fromshare
from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','category','location','title1','description1','image1','title2','description2','image2','title3','description3','image3')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'comment_text']
