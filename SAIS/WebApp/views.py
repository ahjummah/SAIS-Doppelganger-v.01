from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from models import Student, SchoolInfo

def index(request):
	return render(request, 'main.html')

def indexStudent(request):
	return render(request,'indexStudent.html')

def loginPage(request):
	return render(request, 'login.html')

def formLogin(request):
	user = User()
	username = request.POST.get('username')
	print(username)
	password = request.POST.get('password')
	user = authenticate(username = username, password =password)
	if user is not None:
	    # the password verified for the user
	
	  		login(request, user)
	  		return render(request, 'indexStudent.html')
	 
	else:  # Return an 'invalid login' error message.
		print("The username and password were incorrect.")
		return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')

def formRegister(request):
	
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



	return render(request, 'main.html')


# Create your views here.
