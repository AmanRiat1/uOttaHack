from django import forms

class NameForm(forms.Form):
    title= forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())