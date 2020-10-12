from django.shortcuts import render
from . import forms
# Create your views here.
def studentRegisterview(request):
    form = forms.studentRegisteration()
    return render(request, 'formApp/register.html', {'form': form})
