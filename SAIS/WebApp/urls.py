from django.conf.urls import url
from WebApp.views import *	
from . import views

urlpatterns = [
# <<<<<<< HEAD
	url(r'^$', IndexView.as_view(), name='index'),
	url(r'^register$', RegistrationView.as_view(), name = 'register'),
	url(r'^login$', LoginView.as_view(), name = 'login'),
# =======
	# url(r'^$', views.index, name='index'),
	# url(r'^register$', views.register, name = 'register'),
	# url(r'^register/submit$', views.formRegister, name='submitRegister'),
	# url(r'^login$', views.login, name = 'login'),
	# url(r'^login/submit$', views.formLogin, name = 'submitLogin'),
	url(r'^index-S$', StudentView.as_view(), name = 'viewIndex-S'),

# >>>>>>> 0d62c8e8428b6a14d98dd428c8a81f0b8fa8a7f9
]