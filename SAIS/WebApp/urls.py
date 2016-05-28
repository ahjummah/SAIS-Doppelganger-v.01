from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^register$', views.register, name = 'register'),
	url(r'^register/submit$', views.formRegister, name='submitRegister'),
	url(r'^login$', views.loginPage, name = 'login'),
	url(r'^login/submit$', views.formLogin, name = 'submitLogin'),
	url(r'^indexS$', views.indexStudent, name = 'viewIndexStudent'),
	
	
]