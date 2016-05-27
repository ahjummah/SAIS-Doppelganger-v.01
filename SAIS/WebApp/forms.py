from django.forms import ModelForm
from WebApp.models import Student
from WebApp.models import SchoolInfo

class AddStudentForm(ModelForm):
	class Meta:
		model = Student
		fields = ['fname', 'mname', 'lname', 'student_id', 'address']

class AddSchoolInfoForm(ModelForm):
	class Meta:
		model = SchoolInfo
		fields = ['course','year', 'sts_code']
