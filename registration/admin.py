from django.contrib import admin
from .models import User, Student, Faculty, Course, Registration

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Registration)