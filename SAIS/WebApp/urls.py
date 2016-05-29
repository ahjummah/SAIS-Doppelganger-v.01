from django.conf.urls import url
from WebApp.views import *	
from . import views

urlpatterns = [
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register$', RegistrationView.as_view(), name = 'register'),
	url(r'^login$', LoginView.as_view(), name = 'login'),
	url(r'^profile$', StudentView.as_view(), name = 'viewIndexS'),
	url(r'^edit$', EditView.as_view(), name = 'edit'),
	url(r'^logout$', LogoutView.as_view(), name = 'logout'),
	url(r'^addclass$', AddClassView.as_view(), name = 'addclass'),
]