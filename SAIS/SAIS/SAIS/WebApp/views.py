from django.shortcuts import render
from django.http import HttpResponse
import forms

def index(request):
	return render(request, 'main.html')

def register(request):
	return render(request, 'register.html')

def formRegister(request):
	
	newUser = forms.AddStudentForm(request.POST)
	newUser.save()

	return render(request, 'main.html')

# Create your views here.
