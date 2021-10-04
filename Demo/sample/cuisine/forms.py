from django import forms
class ShareCuisineViaEmailForm(forms.Form):
    name = forms.CharField(max_length=25)
    emailFrm = forms.EmailField() #from
    emailTo = forms.EmailField() #to
    emailContent = forms.CharField(required=False,
    widget=forms.Textarea)
