from django.shortcuts import render
from django.http import HttpResponse
from models import Student, SchoolInfo

def index(request):
	return render(request, 'main.html')

def login(request):
	return render(request, 'login.html')

def register(request):
	return render(request, 'register.html')

def formRegister(request):
	
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

# Create your views here.
