from django.shortcuts import render
from django.views.generic import TemplateView, FormView

from .forms import UserLoginForm, UserRegisterForm

class LogInView(FormView):
	form_class = UserLoginForm
	template_name = 'users/login.html'


class UserRegisterView(FormView):
	form_class = UserRegisterForm
	template_name = 'users/register.html'