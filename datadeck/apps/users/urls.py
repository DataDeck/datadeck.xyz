from django.conf.urls import include, url
from .views import LogInView, UserRegisterView

urlpatterns = [
	url(r'^login/$', LogInView.as_view(), name='login'),
	url(r'^registrar/$', UserRegisterView.as_view(), name='register')	
]