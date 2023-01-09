from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    is_admin = models.BooleanField(default=False)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def serialize(self):
        return{
              "id":self.id,
              "username":self.username,
              "is_admin":self.is_admin,
              "is_student":self.is_student,
              "is_teacher":self.is_teacher,
              "first_name":self.first_name,
              "last_name":self.last_name,

        }

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    interest1= models.CharField(max_length=100)
    interest2= models.CharField(max_length=100)
    interest3= models.CharField(max_length=100)
    def serialize(self):
        return{
              "id":self.id,
              "sender":self.sender,
              "receiver":self.receiver,
              "content":self.content
        }



class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    course= models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    description_of_the_course=models.CharField(max_length=1000)
    category=models.CharField(max_length=50)
    def serialize(self):
        return{
              "id":self.id,
              "sender":self.sender,
              "receiver":self.receiver,
              "content":self.content
        }

class Admin(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    position= models.CharField(max_length=100)
    academic_level = models.CharField(max_length=100)
    def serialize(self):
        return{
              "id":self.id,
              "sender":self.sender,
              "receiver":self.receiver,
              "content":self.content
        }

class Course(models.Model):
   teacher=models.ForeignKey("User", on_delete = models.CASCADE, related_name="course")
   course=models.ForeignKey("Teacher", on_delete = models.CASCADE, related_name="coursefers")
   materials=models.CharField(max_length=10000)
   def serialize(self):
       return{
             "id":self.id,
             "sender":self.sender,
             "receiver":self.receiver,
             "content":self.content
       }



class Relation(models.Model):
     interest=models.CharField(max_length=100)
     def serialize(self):
         return{
               "id":self.id,
               "sender":self.sender,
               "receiver":self.receiver,
               "content":self.content
         }

class CourseRegistered(models.Model):
    teacher=models.ForeignKey("User", on_delete = models.CASCADE, related_name="Betters")
    student=models.ForeignKey("User", on_delete = models.CASCADE, related_name="nicers")
    course=models.ForeignKey("Teacher", on_delete = models.CASCADE, related_name="googlers")
    def serialize(self):
        return{
              "id":self.id,
              "sender":self.sender,
              "receiver":self.receiver,
              "content":self.content
        }

class Message(models.Model):
    sender=models.ForeignKey("User", on_delete = models.CASCADE, related_name="boomers")
    receiver=models.ForeignKey("User", on_delete = models.CASCADE, related_name="Bests")
    content=models.CharField(max_length=300)
    def serialize(self):
        return{
              "id":self.id,
              "sender":self.sender.serialize(),
              "receiver":self.receiver.serialize(),
              "content":self.content
        }


class Upload(models.Model):
    instructor=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    uploaded=models.FileField(upload_to='books/pdfs')
