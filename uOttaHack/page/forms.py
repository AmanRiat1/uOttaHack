from django import forms

<<<<<<< HEAD
from . models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
=======
class NameForm(forms.Form):
    title= forms.CharField(widget=forms.TextInput())
    author = forms.CharField(widget=forms.TextInput())
>>>>>>> 4751f810dcbaea1ab594834a78889f0f251ab8bd
