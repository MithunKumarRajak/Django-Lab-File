from django import forms
from .models import Student, Course


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'email', 'courses']
        widgets = {
            'courses': forms.CheckboxSelectMultiple,
        }


class CourseSelectForm(forms.Form):
    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        label="Select Course",
        required=True
    )
