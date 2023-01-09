from django.urls import path


from . import views




urlpatterns = [

    path("", views.index, name="index"),
    path("logged", views.logged, name="logged"),
    path("comments/<int:id>",views.comments,name="comments"),
    path("commentsByTeacher/<str:message>",views.commentsByTeacher,name="commentsByTeacher"),
    path("receivingComments",views.receivingComments,name="receivingComments"),
    path("search",views.search,name="search"),
    path("eachCourse/<int:teacher_id>/",views.eachCourse,name="eachCourse"),
    path("seeingMats/<str:click>",views.seeingMats,name="mats"),
    path("TeacherRegistered",views.TeacherRegistered,name="TeacherRegistered"),
    path("newInterest",views.newInterest,name="newInterest"),
    path("upload_list",views.upload_list,name="upload_list"),
    path("books/upload",views.upload_book,name="upload_book"),
    path("student_register",views.student_register,name="student_register"),
    path("teacher_register",views.teacher_register,name="teacher_register"),
    path("admin_register",views.admin_register,name="admin_register"),
    path("register", views.register, name="register"),
    path("accounts/login/", views.login_view, name="logined"),
    path("login", views.login_view, name="login"),
    path("logout",views.logout_view,name="logout")
]
