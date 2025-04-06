from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('faculty/', views.faculty_dashboard, name='faculty_dashboard'),
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('register/', views.register_course, name='register_course'),
    path('register-faculty/', views.register_faculty, name='register_faculty'),
    path('register-student/', views.register_student, name='register_student'),
    path('logout/', views.logout_view, name='logout'),
]