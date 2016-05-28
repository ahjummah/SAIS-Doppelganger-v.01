from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from WebApp.models import Student, SchoolInfo

class IndexView(View):
	
	def get(self, request):
		return render(self.request, 'main.html')

class LoginView(View):

	def get(self, request):
		return render(request, 'login.html')

class RegistrationView(View):
	
	def get(self, request):
		return render(request, 'register.html')

	def post(self, request):
		student = Student()
		studentInfo = SchoolInfo()
		student.fname = request.POST['fname']
		student.mname = request.POST['mname']
		student.lname = request.POST['lname']
		student.student_id = request.POST['student_id']
		student.address = request.POST['address']
		student.gender = request.POST['gender']
		student.maritalstatus = request.POST['maritalstatus']
		student.save()
		studentInfo.student_id = student
		studentInfo.course = request.POST['course']
		studentInfo.year = request.POST['year']
		studentInfo.sts_code = request.POST['sts_code']
		studentInfo.save()

		return render(request, 'main.html')