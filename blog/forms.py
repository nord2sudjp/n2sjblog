from django import forms
from blog.models import Post, Comment


class PostForm(form.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        wiedgets = {
                'title':forms.TextInput(attrs = {'class':'textinputclass'}),
                'text':forms.TextArea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('author', 'text')

        wiedgets = {
                'author':forms.TextInput(attrs = {'class':'textinputclass'}),
                'text':forms.TextArea(attrs={'class':'editable medium-editor-textarea '})
        }
