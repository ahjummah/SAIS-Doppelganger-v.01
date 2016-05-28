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
		return render(self.equest,'indexStudent.html')

# def indexStudent(request):
# 	return render(request,'indexStudent.html')

# def login(request):
# 	return render(request, 'login.html')

class LoginView(View):
	"""docstring for LoginView"""
	def get(self, request):
		user = User()
		username = request.POST.get('student_id', False)
		password = request.POST.get('password', False)
		user = authenticate(username = username, password =password)
		if user is not None:
		    # the password verified for the user
		
		  		login(request, user)
		  		return render(self.request, 'indexStudent.html')
		 
		else:  # Return an 'invalid login' error message.
			print("The username and password were incorrect.")
			return render(self.request, 'login.html')

	def post(self,request):
		user = User()
		username = request.POST.get('student_id', False)
		password = request.POST.get('password', False)
		user = authenticate(username = username, password =password)
		if user is not None:
		    # the password verified for the user
		
		  		login(request, user)
		  		return render(self.request, 'indexStudent.html')
		 
		else:  # Return an 'invalid login' error message.
			print("The username and password were incorrect.")
			return render(self.request, 'login.html')



	# def formLogin(request):
	# 	user = User()
	# 	username = request.POST.get('student_id', False)
	# 	password = request.POST.get('password', False)
	# 	user = authenticate(username = username, password =password)
	# 	if user is not None:
	# 	    # the password verified for the user
		
	# 	  		login(request, user)
	# 	  		return render(self.request, 'indexStudent.html')
		 
	# 	else:  # Return an 'invalid login' error message.
	# 		print("The username and password were incorrect.")
	# 		return render(self.request, 'login.html')

# def register(request):
# 	return render(request, 'register.html')

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

		return render(self.request, 'main.html')

	# student = Student()
	# studentInfo = SchoolInfo()
	# user = User()

	# student.fname = request.POST['fname']
	# student.mname = request.POST['mname']
	# student.lname = request.POST['lname']
	# student.student_id = request.POST['student_id']
	# student.address = request.POST['address']
	# student.gender = request.POST['gender']
	# student.maritalstatus = request.POST['maritalstatus']
	# student.email = request.POST['email']
	# student.save()

	# studentInfo.student_id = student
	# studentInfo.course = request.POST['course']
	# studentInfo.year = request.POST['year']
	# studentInfo.sts_code = request.POST['sts_code']
	# studentInfo.save()

	# user = User.objects.create_user(student.student_id, request.POST['email'], request.POST['password'])
	# user.last_name = student.lname
	# user.first_name = student.fname
	# user.save()

# Create your views here.
