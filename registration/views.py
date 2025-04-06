from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Course, Student, Faculty, Registration, User
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib import messages


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.is_faculty:
                return redirect('faculty_dashboard')
            elif user.is_student:
                return redirect('student_dashboard')
            else:
                return HttpResponse("Role not assigned.")
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def faculty_dashboard(request):
    if not request.user.is_faculty:
        return redirect('login')

    faculty = Faculty.objects.get(user=request.user)

    if request.method == 'POST':
        name = request.POST['name'].strip()
        code = request.POST['code'].strip()

        # Check if course name or code already exists for this faculty
        if Course.objects.filter(name__iexact=name, offered_by=faculty).exists():
            messages.error(request, f"A course with the name '{name}' already exists.")
        elif Course.objects.filter(code__iexact=code, offered_by=faculty).exists():
            messages.error(request, f"A course with the code '{code}' already exists.")
        else:
            Course.objects.create(name=name, code=code, offered_by=faculty)
            messages.success(request, f"Course '{name}' has been successfully added.")

    courses = Course.objects.filter(offered_by=faculty)
    return render(request, 'faculty_dashboard.html', {'courses': courses})

@login_required
def student_dashboard(request):
    if not request.user.is_student:
        return redirect('login')
    student = Student.objects.get(user=request.user)
    registrations = Registration.objects.filter(student=student)
    return render(request, 'student_dashboard.html', {'registrations': registrations})

@login_required
def register_course(request):
    if not request.user.is_student:
        return redirect('login')
    student = Student.objects.get(user=request.user)
    if Registration.objects.filter(student=student).count() >= 2:
        return redirect('student_dashboard')
    courses = Course.objects.exclude(registration__student=student)
    if request.method == 'POST':
        course_id = request.POST['course_id']
        course = Course.objects.get(id=course_id)
        Registration.objects.create(student=student, course=course)
        return redirect('student_dashboard')
    return render(request, 'register_course.html', {'courses': courses, 'student': student})

@csrf_exempt
def register_faculty(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        mobile_number = request.POST['mobile_number']
        faculty_id = request.POST['faculty_id']
        department = request.POST['department']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register_faculty')

        if Faculty.objects.filter(faculty_id=faculty_id).exists():
            messages.error(request, 'Faculty ID already exists')
            return redirect('register_faculty')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            dob=dob,
            mobile_number=mobile_number,
            is_faculty=True,
            password=make_password(password)
        )
        Faculty.objects.create(user=user, faculty_id=faculty_id, department=department)

        messages.success(request, 'Faculty registered successfully. Please login.')
        return redirect('login')

    return render(request, 'register_faculty.html')

@csrf_exempt
def register_student(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        dob = request.POST['dob']
        mobile_number = request.POST['mobile_number']
        student_id = request.POST['student_id']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register_student')

        user = User.objects.create(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=make_password(password),
            is_student=True,
            dob=dob,
            mobile_number=mobile_number,
        )

        Student.objects.create(user=user, student_id=student_id)
        messages.success(request, 'Student registered successfully. Please login.')
        return redirect('login')

    return render(request, 'register_student.html')

def logout_view(request):
    auth_logout(request)
    return redirect('login')