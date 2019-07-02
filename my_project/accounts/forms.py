from django import forms
from .models import CustomUser

class UpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('user_rollno', 'user_department', 'user_hostel','user_contact')
