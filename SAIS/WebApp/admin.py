from django.contrib import admin

from WebApp import models

# Register your models here.
admin.site.register(models.Student)
admin.site.register(models.SchoolInfo)
admin.site.register(models.Subjects)
admin.site.register(models.Account)
admin.site.register(models.Schedule)