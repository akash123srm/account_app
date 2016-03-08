from django import forms
from django.forms import ModelForm
from .models import UserProfile


class UserProfileForm(ModelForm):
      class Meta:

          model = UserProfile
          fields = ['first_name', 'last_name', 'iban']

          labels = {
              'first_name': 'Please enter your first name.',
              'last_name': 'Please enter your last name.',
              'iban': 'Please enter your iban number'
          }

          widgets = {
            'first_name': forms.TextInput(),
            'last_name': forms.TextInput(),
            'iban': forms.TextInput()
            }
