from django.db import models

# Create your models here.
from django import forms

Sex_choice = (
    ('level1', 'Male'),
    ('level2', 'Female')
)

class RegisterForm(forms.Form):
    username = forms.CharField(label='username', max_length=20)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    age = forms.CharField(label='age', widget=forms.NumberInput)
    sex = forms.ChoiceField(label="sex", choices=Sex_choice)
    email = forms.EmailField(label='email')


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=200)
    age = models.CharField(max_length=10)
    sex = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
