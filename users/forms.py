from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
#importing profile model for profile pictures
from .models import Profile

#inherit
class UserRegisterForm(UserCreationForm):
	email=forms.EmailField()
#form interact with which model
#keep configurations at one place
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	email=forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model=Profile
		fields=['image']