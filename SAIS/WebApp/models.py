from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
	fname = models.CharField(max_length=20, null=True, blank = True)
	mname = models.CharField(max_length=20, null=True, blank = True)
	lname = models.CharField(max_length=20, null=True, blank = True)
	user_id = models.OneToOneField(User, null=True, blank=True)
	student_id = models.CharField(max_length=10, null=True, blank = True) #PK
	address = models.CharField(max_length = 10, null=True, blank = True)
	gender = models.CharField(max_length = 10, null=True, blank = True)
	maritalstatus = models.CharField(max_length = 15, null=True, blank = True)
	email = models.CharField(max_length=30 , null = True, blank = True)

	def __str__(self):
		return str(self.student_id) + " : " + str(self.lname)

class SchoolInfo(models.Model):
	student_id = models.ForeignKey('Student')
	course = models.CharField(max_length = 20, null=True, blank = True)
	year = models.IntegerField(null=True, blank = True)
	sts_code = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return str(self.student_id) + " Info"

class Subjects(models.Model):
	subject_code = models.CharField(max_length=20, null=True, blank=True)
	cluster_code = models.CharField(max_length=20, null=True, blank=True)
	prof_id = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return str(self.subject_code)

class Schedule(models.Model):
	subject_id = models.ForeignKey('Subjects')
	day = models.CharField(max_length=10, null=True, blank=True)
	time = models.CharField(max_length=20, null=True, blank=True)

	def __str__(self):
		return str(self.subject_id) + " : " +str(self.day) +" "+ str(self.time) 

class Enrolled(models.Model):
	student_id = models.ForeignKey('Student')
	subject_code = models.ForeignKey('Subjects')

class Account(models.Model):
	student_id = models.ForeignKey('SchoolInfo')
	transactions = models.CharField(max_length=20, null=True, blank=True)#Payment or Loan#
	amount = models.FloatField(null=True, blank=True)
	


