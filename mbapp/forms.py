from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Employee


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    address = forms.CharField(required=False, max_length=200)
    

    class Meta:
        model = get_user_model()
        fields = ('email', 'password1', 'password2','first_name', 'last_name', 'company','address',)

class AddEmpForm(forms.Form):
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    address = forms.CharField(required=False, max_length=200)

class UpdateEmpForm(forms.ModelForm):
    class Meta:  
        model = Employee  
        fields = ('fname', 'lname', 'company', 'address')
