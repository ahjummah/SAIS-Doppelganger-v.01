from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import View, DetailView
from WebApp.models import Student, SchoolInfo, Subjects
from django.template import Context
class IndexView(View):
	
	def get(self, request):	
		return render(self.request, 'main.html')
		
class LoginView(View):

	def get(self, request):
		return render(self.request, 'login.html')

class StudentView(View):

	def get(self, request):
		context = {}
		context['user'] = request.user
		return render(self.request,'indexStudent.html',context=context)

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
		  		return redirect('WebApp:viewIndexS')
		 
		else:  # Return an 'invalid login' error message.
			print("The username and password were incorrect.")
			return render(self.request, 'login.html')

class LogoutView(View):
	def get(self, request):
		return redirect('WebApp:logout')	

	def post(self, request):
		logout(request, user)
		

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

class AddClassView(View):

	def get(self, request):
		return render(self.request, 'AddClass.html')


	def post(self, request):
		keyword = request.POST.get('searchbox')
		print("Keyword is: " + keyword)
		context = {}
		context['subjectcode'] = Subjects.objects.filter(subject_code__icontains=keyword)
		return render(self.request,'AddClass.html',context=context)

class EditView(View):
	
	def get(self, request):

	    student_object = Student.objects.filter(user_id=request.user)
	    schoolinfo_object = SchoolInfo.objects.filter(student_id=student_object)
	   

	    dictionary = {
	    	'firstname': student_object.get().fname,
	    	'middlename': student_object.get().mname,
	    	'lastname': student_object.get().lname,
	    	'address': student_object.get().address,
	    	'gender': student_object.get().gender,
	    	'maritalstatus': student_object.get().maritalstatus,
	    	'student_id': student_object.get().student_id,
	    	'email': student_object.get().email,
	    	'course': schoolinfo_object.get().course,
	    	'year': schoolinfo_object.get().year,
	    	'sts_code': schoolinfo_object.get().sts_code,
	    	}
	    return render(self.request, 'EditProfile.html', dictionary)

	def post(self, request):

		return render(self.request, 'main.html')
	
		
