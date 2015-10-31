# -*- encoding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.Form):

	username = forms.CharField(max_length=30,
							widget= forms.TextInput(attrs={
								'class' : 'form-control',
								'placeholder' : 'Ingresa tu Usuario',
								'required' : 'True'
							}))

	password = forms.CharField(max_length=30,
							widget = forms.PasswordInput(attrs={
								'class' : 'form-control',
								'placeholder' : 'Ingresa tu Contraseña',
								'required' : 'True'
							}))

	def clean(self):
		if self.cleaned_data.get('username') and self.cleaned_data.get('password'):
			username = self.cleaned_data.get('username')
			username_exist = User.objects.filter(username = username).exists()
			if username_exist:
				user = User.objects.get(username = username)
				if not user.check_password(self.cleaned_data.get("password")):
					self.add_error('password', 'La contraseña es incorrecta')
			else:
				self.add_error('username', 'El usuario no existe!')


class UserRegisterForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ('username', 'email', 'password')
		widgets = {
			'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingresa un nombre de Usuario'}),
			'email' : forms.EmailInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingresa tu Emai'}),
			'password' : forms.PasswordInput(attrs={'class' : 'form-control', 'placeholder' : 'Ingresa una Contraseña'}),
		}