from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.generic import View
from WebApp.models import Student, SchoolInfo

class IndexView(View):
	
	def get(self, request):
		return render(self.request, 'main.html')

class LoginView(View):

	def get(self, request):
		return render(self.request, 'login.html')

class StudentView(View):

	def get(self, request):
		return render(self.request,'indexStudent.html')

class LoginView(View):
	"""docstring for LoginView"""
	def get(self, request):
		return render(self.request, 'login.html')

	def post(self, request):
		user = User()
		username = request.POST.get('student_id')
		password = request.POST.get('password')
		username = Student.objects.get(student_id=username)
		username = username.user_id.username
		user = authenticate(username = username, password =password)
		if user is not None:
		    # the password verified for the user
		
		  		login(request, user)
		  		return render(self.request, 'indexStudent.html')
		 
		else:  # Return an 'invalid login' error message.
			print("The username and password were incorrect.")
			return render(self.request, 'login.html')

class RegistrationView(View):
	
	def get(self, request):
		return render(self.request, 'register.html')

	def post(self, request):
		student = Student()
		studentInfo = SchoolInfo()
		user = User()

		student.fname = request.POST['fname']
		student.mname = request.POST['mname']
		student.lname = request.POST['lname']
		student.student_id = request.POST['student_id']
		student.address = request.POST['address']
		student.gender = request.POST['gender']
		student.maritalstatus = request.POST['maritalstatus']
		student.email = request.POST['email']
		student.save()

		studentInfo.student_id = student
		studentInfo.course = request.POST['course']
		studentInfo.year = request.POST['year']
		studentInfo.sts_code = request.POST['sts_code']
		studentInfo.save()

		user = User.objects.create_user(student.student_id, request.POST['email'], request.POST['password'])
		user.last_name = student.lname
		user.first_name = student.fname
		user.save()

		student.user_id = user;
		student.save()

		return render(self.request, 'main.html')
