from django.contrib import admin

from .models import User,  Student, Teacher, Admin,Course,Relation,CourseRegistered,Message,Upload

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Admin)
admin.site.register(Course)
admin.site.register(Relation)
admin.site.register(CourseRegistered)
admin.site.register(Message)
admin.site.register(Upload)
