from .models import Post, Comment
from django import forms 

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'image',
            'caption'
        ]
    
class CommentCreateForm(forms.ModelForm): #Formulario para introducir comentarios a los post
    class Meta:
        model = Comment
        fields = [
            'text'
        ]