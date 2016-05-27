from django.db import models

# Create your models here.
class Student(models.Model):
	fname = models.CharField(max_length=20, null=True, blank = True)
	mname = models.CharField(max_length=20, null=True, blank = True)
	lname = models.CharField(max_length=20, null=True, blank = True)
	user_id = models.IntegerField(null=True, blank = True)
	student_id = models.CharField(max_length=10, null=True, blank = True) #PK
	address = models.CharField(max_length = 10, null=True, blank = True)

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
	schedule_id = models.IntegerField(null=True, blank=True)

class Schedule(models.Model):
	schedule_id = models.ForeignKey('Subjects')
	day = models.CharField(max_length=10, null=True, blank=True)
	time = models.CharField(max_length=20, null=True, blank=True)

class Account(models.Model):
	student_id = models.ForeignKey('SchoolInfo')
	transactions = models.CharField(max_length=20, null=True, blank=True)#Payment or Loan#
	amount = models.FloatField(null=True, blank=True)
	


