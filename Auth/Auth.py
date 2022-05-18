from django import forms
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email","password1", "password2"]
class LoginForm(AuthenticationForm):
	class Meta:
		model = User
		fields = ["username", "password1"]