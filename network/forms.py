from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User,Student,Teacher,Admin,Course,Upload

class studentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    interest1 = forms.CharField(required=True)
    interest2 = forms.CharField(required=True)
    interest3 = forms.CharField(required=True)


    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.interest1=self.cleaned_data.get('interest1').lower()
        student.interest2=self.cleaned_data.get('interest2').lower()
        student.interest3=self.cleaned_data.get('interest3').lower()
        student.save()
        return user

class teacherSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    course = forms.CharField(required=True)
    academic_level = forms.CharField(required=True)
    description_of_the_course=forms.CharField(required=True)
    category=forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        teacher =Teacher.objects.create(user=user)
        teacher.course=self.cleaned_data.get('course').lower()
        teacher.academic_level=self.cleaned_data.get('academic_level')
        teacher.description_of_the_course=self.cleaned_data.get('description_of_the_course')
        teacher.category=self.cleaned_data.get('category').lower()
        teacher.save()
        return user

class adminSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    position = forms.CharField(required=True)
    academic_level = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = True
        user.is_staff = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        admin = Admin.objects.create(user=user)
        admin.position=self.cleaned_data.get('position')
        admin.academic_level=self.cleaned_data.get('academic_level')
        admin.save()
        return user

class BookForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('instructor','subject','uploaded')
