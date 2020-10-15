from django import forms
from testapp.models import moviemodel

class movieform(forms.ModelForm):
    class Meta:
        model = moviemodel
        fields = '__all__'