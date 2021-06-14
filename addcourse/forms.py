from django import forms
from .models import AddCourse



class AddCourseForm(forms.ModelForm):
    class Meta:
        model = AddCourse
        fields = '__all__'
        exclude = ('is_published',)
        widgets = {
            'user_id': forms.HiddenInput(attrs={
                'class': 'form-control form-control3',
                'id': 'user_id',
                'placeholder': 'User Id'
            }),
        }

    


