from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={"placeholder": "Your name"}))
    school = forms.CharField(label='',
                             widget=forms.TextInput(attrs={"placeholder": "Your school"}))
    course = forms.CharField(label='',
                             widget=forms.TextInput(attrs={"placeholder": "Name of the course"}))


    class Meta:
        model = Student
        fields = [
            'name',
            'school',
            'course'
        ]
