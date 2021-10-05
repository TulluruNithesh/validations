from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower()=='a':
        raise forms.ValidationError('value should not starts with a')

def check_for_len(value):
    if len(value)>5:
        raise forms.ValidationError('len should not exeed 5')

def check_for_age(value):
    if value<18 or value>45:
        raise forms.ValidationError('age should not in middle of 18,45')




class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_a,check_for_len])
    age=forms.IntegerField(validators=[check_for_age])
    email=forms.EmailField(max_length=100)
    reenteremail=forms.EmailField(max_length=100)

    def clean(self ):
        e=self.cleaned_data['email']
        r=self.cleaned_data['reenteremail']
        if e!=r:
           raise forms.ValidationError('age should not in middle of 18,45') 
