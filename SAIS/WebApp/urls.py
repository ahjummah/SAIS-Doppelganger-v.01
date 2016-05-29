from django.conf.urls import url
from WebApp.views import *	
from . import views

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register$', RegistrationView.as_view(), name = 'register'),
	url(r'^login$', LoginView.as_view(), name = 'login'),
	url(r'^index-S$', StudentView.as_view(), name = 'viewIndex-S'),
	url(r'^edit$', EditView.as_view(), name = 'edit'),
]