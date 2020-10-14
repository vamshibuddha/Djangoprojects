from django.shortcuts import render
from . import forms
# Create your views here.
def studentview(request):
    form = forms.StudentForm()
    if request.method == 'POST':
        form = forms.StudentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('Form data inserted into DB successfully')
    return render(request, 'testapp/student.html', {'form': form})
