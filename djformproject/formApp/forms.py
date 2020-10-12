from django import forms

class studentRegisteration(forms.Form):
    names = forms.CharField()
    marks = forms.IntegerField()

