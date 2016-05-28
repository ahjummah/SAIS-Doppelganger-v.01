from django.conf.urls import url
from WebApp.views import *	
from . import views

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register$', RegistrationView.as_view(), name = 'register'),
	url(r'^register/submit$', views.formRegister, name='submitForm'),
	url(r'^login$', LoginView.as_view(), name = 'login'),
]