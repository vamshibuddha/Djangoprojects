from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name = forms.CharField()
    rollno = forms.IntegerField()
    email = forms.EmailField()
    feedback = forms.CharField(widget=forms.Textarea, validators=[validators.MaxLengthValidator(40)
                               , validators.MinLengthValidator(6)])

    def clean(self):
        cleaned_data = super().clean()
        inputname = self.cleaned_data['name']
        if len(inputname) < 5:
            raise forms.ValidationError('Name should be minimum 5 charaters')

        '''  def clean_name(self):
        inputname = self.cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError('The length of name field should be >=4')
        return inputname

        def clean_rollno(self):
        inputrollo = self.cleaned_data['rollno']
        print('validating  rollno')
        return inputrollo

    def clean_email(self):
        inputemail = self.cleaned_data['email']
        print('Validating email')
        return inputemail

    def clean_feedback(self):
        inputfeedback = self.cleaned_data['feedback']
        print('Validating feedback')
        return inputfeedback 
         def starts_with_d(value):
    if value[0].lower() != 'd':
        raise forms.ValidationError('Name should be starts with d')
    def name_only_abc(value):
    if value.isalpha() != True:
        raise forms.ValidationError('Name should only be alphabets')
    def gmail_verfication(value):
    if value[len(value)-9:] != 'gmail.com':
        raise forms.ValidationError('Mail must be gmail')
        '''


