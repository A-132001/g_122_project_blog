from .models import Comment,Post
from django import forms 

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        
        
# class PostForm(forms.Form):
#     title = forms.CharField(max_length=100)
#     content = forms.CharField(widget=forms.Textarea)
#     image = forms.FileField(required=True)
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','content','image','is_published']



        
    