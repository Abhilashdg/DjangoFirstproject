from django import forms

from .models import Comment
class ShareCuisineViaEmailForm(forms.Form):
    name = forms.CharField(max_length=25)
    emailFrm = forms.EmailField() #from
    emailTo = forms.EmailField() #to
    emailContent = forms.CharField(required=False,
    widget=forms.Textarea)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')
