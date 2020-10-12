from django.shortcuts import render
from . import forms
# Create your views here.

def feedback_view(request):
    form = forms.FeedbackForm()
    if request.method == 'POST':
        form = forms.FeedbackForm(request.POST)
        if form.is_valid():
            print('Form validation success and printing feedback info')
            print('Student Name:', form.cleaned_data['name'])
            print('Student Rollno:', form.cleaned_data['rollno'])
            print('Student mail id', form.cleaned_data['email'])
            print('Student Feedback:', form.cleaned_data['feedback'])
            return render(request, 'testApp/thankyou.html', {'name': form.cleaned_data['name']})

    return render(request, 'testApp/feedback.html', {'form': form})
