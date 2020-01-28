from django import forms
from tinymce import TinyMCE
from .models import Post




class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class PostForm(forms.ModelForm):
    content = forms.CharField(
        widget=TinyMCEWidget(
            attrs={'required': False, 'cols': 30, 'rows': 10}
        )
    )

    class Meta:
        model = Post
        fields = ('title', 'overview', 'content', 'thumbnail',
        'categories', 'featured')

# class CommentForm(forms.ModelForm):
#     user = forms.CharField(widget=forms.TextInput(attrs={'class':'form-group col-md-6 form-control', 'placeholder':'Name','id':'username'}))
#     email = forms.CharField(widget=forms.EmailInput(attrs={'class':'form-group col-md-6 form-control','placeholder':'Email Address (will not be published)','id':'useremail'}))
#     content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder':'Type your comment','id':'usercomment', 'rows':'4'}))
#     class Meta:
#         model = Comment
#         fields = ['user','email','content']
