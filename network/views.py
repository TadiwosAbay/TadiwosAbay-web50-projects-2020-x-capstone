import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,HttpResponse, HttpResponseRedirect
from django.forms import inlineformset_factory
from django.urls import reverse
from django.views.generic import CreateView
from .models import Student,Teacher,Admin,Course,Relation,CourseRegistered,Message
from .models import User
from .forms import studentSignUpForm,teacherSignUpForm,adminSignUpForm,BookForm,Upload
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages



def index(request):
    return render(request,"network/login.html",{
    "form":AuthenticationForm()
    })

def register(request):
    return render(request,"network/register.html")

def student_register(request):
    model = User
    mobiles=Relation.objects.all()

    form = studentSignUpForm()
    if request.method=='POST':
        form = studentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"network/login.html",{
            "form":AuthenticationForm()
            })
    else:
         return render(request,"network/student_register.html",{
         "form":form,"mobiles":mobiles
       })

def teacher_register(request):
    form = teacherSignUpForm()
    if request.method=='POST':
        form = teacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"network/login.html",{
            "form":AuthenticationForm()
            })

    else:
          return render(request,"network/teacher_register.html",{
           "form":form
         })

def admin_register(request):
    form = adminSignUpForm()
    if request.method=='POST':
        form = adminSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"network/login.html",{
            "form":AuthenticationForm()
            })
    else:
         return render(request,"network/admin_register.html",{
         "form":form
        })

def login_view(request):
#     page that will be used to login
    if request.method=='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request,username=username, password=password)

            if user is not None :
                login(request,user)
                return HttpResponseRedirect(reverse('logged'))

            else:
                return render(request, "network/login.html",{
                    'form':AuthenticationForm(),"message":"Invalid username/password"
                    })
        else:
            return render(request, "network/login.html",{
            'form':AuthenticationForm(),"message":"Invalid username/password"
            })
    else:
        return render(request, "network/login.html",
            context={'form':AuthenticationForm()})

@login_required
def logged(request):
#     page whe login:
    #   students-course list based on their choices
    user=User.objects.get(username=request.user)
    if user.is_student:
        print(f"{request.user}")
        choices=Student.objects.filter(user=user.id)
        choice1=choices[0].interest1.lower()
        choice2=choices[0].interest2.lower()
        choice3=choices[0].interest3.lower()
        courses=Teacher.objects.filter(category=choice1)
        coursders=Teacher.objects.filter(category=choice2)
        courss=Teacher.objects.filter(category=choice3)
        return render(request,"network/course.html",{
        "courses":courses,"coursders":coursders,"courss":courss,"user":user
          })
    elif user.is_teacher:
        return render(request,"network/teacher.html",{
        })
    else:
        return render(request,"network/admin.html")

@login_required
def search(request):
#     to search for courses-will return the courses searched for 
    # and the teachers who will give the courses
    
    key=request.POST['searc']
    x=key
    matches=[]
    senders=User.objects.filter(username=request.user)
    sender=senders[0]
    main_admins=Admin.objects.all()
    exacts=Teacher.objects.filter(course__iexact=x)
    all_courses=Course.objects.all()
    contains = Teacher.objects.exclude(pk__in=exacts).filter(course__contains=key)
    check=False
    if exacts.count()==0:
        if contains.count()==0:
            check=True
            for main_admin in main_admins:
                Message.objects.create(sender=sender,receiver=main_admin.user,content="a course named "+request.POST['searc']+" was searched but couldn't found!!!")
    return render(request,"network/search.html",{
     "exacts":exacts,"contains":contains,"check":check
    })

@login_required
def seeingMats(request,click):
#     Teachers will see the courses they give and specific materials 
    # and add new materials to the courses
    
    teacher=User.objects.get(username=request.user)
    x=request.user
    course=Teacher.objects.get(user=teacher)
    notes=[]
    if click=="seeAll":
        assignments=Course.objects.filter(teacher=teacher,course=course)
        for assignment in assignments:
            notes.append(assignment.materials)
        return  JsonResponse({'assis':notes})
    else:
        assign=Course.objects.create(teacher=teacher,course=course,materials=click)
        assignments=Course.objects.filter(teacher=teacher,course=course)
        for assignment in assignments:
            notes.append(assignment.materials)
        return  JsonResponse({'assis':notes})

@login_required
def eachCourse(request,teacher_id):
#    students will search for a course,if they are already registered for the course they will see course material,
#     if want to newly register, will register for the course and will see course materials
#     if want to audit the course before registering, they will do so.

    teacher=User.objects.get(pk=teacher_id)
    student=User.objects.get(username=request.user)
    teach=Teacher.objects.get(user=teacher)
    already_registered=CourseRegistered.objects.filter(teacher=teacher,student=student,course=teach)
    materials=Course.objects.filter(teacher=teacher)
    books=Upload.objects.filter(instructor=teach.user.username)
    if already_registered :
        return render(request,"network/courseRegistered.html",{
         "materials":materials,"teach":teach,"books":books
      })

    else:
        if request.method=='POST':
            CourseRegistered.objects.create(teacher=teacher,student=student,course=teach)
            return render(request,"network/courseRegistered.html",{
             "materials":materials,"teach":teach,"books":books
          })
        else:
             return render(request,"network/each_course.html",{
                 "teach":teach
               })



@login_required
def TeacherRegistered(request):
#     Teachers will see the students registered for the course 
#     and students will see the courses they are registered for.

    user=User.objects.get(username=request.user)
    if user.is_teacher:
        students=CourseRegistered.objects.filter(teacher=user)
        collects=[]
        for student in students:
            collects.append(student.student.first_name)
        return JsonResponse({'collects':collects})
    elif user.is_student:
        courses=CourseRegistered.objects.filter(student=user)
        return render(request,"network/RegisteredCourses.html",{
        "courses":courses
        })

@login_required
def comments(request,id):
#     students--> admins,and teachers
   

    student=User.objects.get(username=request.user)
    teacher=Course.objects.filter(teacher=id)

    main_admins=Admin.objects.all()
    if id==student.id:
        if request.method=='POST':
            message=request.POST['conten']
            for main_admin in main_admins:
                Message.objects.create(sender=student,receiver=main_admin.user,content=message)
            return render(request,"network/success.html")
        else:
            return render(request,"network/comments.html",{
            "student":student
            })
    else:
        message=request.POST['conten']
        teacherName=teacher[0].teacher
        Message.objects.create(sender=student,receiver=teacherName,content=message)
        return render(request,"network/success.html")

@login_required
def commentsByTeacher(request,message):
#     teachers-->admins

    senders=User.objects.filter(username=request.user)
    sender=senders[0]
    main_admins=Admin.objects.all()
    for main_admin in main_admins:
        Message.objects.create(sender=sender,receiver=main_admin.user,content=message)
    return JsonResponse({'messag':"Your message has been sent"})

@login_required
def receivingComments(request):
#     any user could see comments given to him

    receiver=User.objects.get(username=request.user)
    messages=Message.objects.filter(receiver=receiver)
    comments=[]
    for message in messages:
       comment=message.serialize()
       comments.append(comment)
    return JsonResponse({'messag':comments})

@login_required
def upload_book(request):
#     Teachers will upload course materials for students

    user=User.objects.filter(username=request.user)
    name=user[0]
    cours=Teacher.objects.filter(user=name.id)
    cour=cours[0]

    if request.method=='POST':
        form=BookForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('upload_list'))

    else:
        form=BookForm()
        return render(request,"network/upload_book.html",{
        "form":form
        })

@login_required
def upload_list(request):
#     Teachers could see the materials uploaded to them.

    books=Upload.objects.filter(instructor=request.user)
    return render(request,"network/book_list.html",{
    "books":books
    })

@login_required
def newInterest(request):
#     students will search for courses they are interested in
    courses=Teacher.objects.all()
    fields=Relation.objects.all()
    existingFields=[]
    for field in fields:
        existingFields.append(field.interest)
    newInterests=[]
    for course in courses:
        if course.category not in existingFields and course.category not in newInterests:
            newInterests.append(course.category)

    if newInterests==[]:
        return JsonResponse({'message':"The system has found no new fields"})
    else:
        for interest in newInterests:
            Relation.objects.create(interest=interest)
        return JsonResponse({'message':"The system has found new fields and added them to the table"})



@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))
