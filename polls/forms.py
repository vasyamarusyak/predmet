from django import forms
from .models import Question

class PostForm(forms.Form):
    for field in range(len(Question.objects.values())):
        print(field)
    question1 = forms.IntegerField(required=False)
    question2 = forms.IntegerField(required=False)
    question3 = forms.IntegerField(required=False)
    question4 = forms.IntegerField(required=False)
    question5 = forms.IntegerField(required=False)
    question6 = forms.IntegerField(required=False)
    question7 = forms.IntegerField(required=False)
    question8 = forms.IntegerField(required=False)
    question9 = forms.IntegerField(required=False)
    question10 = forms.IntegerField(required=False)
