from django.forms import ModelForm
from WebApp.models import Student

class AddStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['fname', 'mname', 'lname', 'student_id', 'address']
