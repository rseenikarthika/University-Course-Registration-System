# University Course Registration System

A web-based system built with Django to manage student and faculty registration and allow students to register for available courses.

---

## 🚀 Features

- Student and Faculty Registration with validation
- User Authentication (Login/Logout)
- Faculty course creation (extendable)
- Student course registration (up to 2 max)
- Dashboard for viewing registered courses
- Role-based user handling (student/faculty)

---

## 🖥️ Live Pages

- [Login](http://localhost:8000/login/)
- [Register as Student](http://localhost:8000/register_student/)
- [Register as Faculty](http://localhost:8000/register_faculty/)
- [Course Registration (Student)](http://localhost:8000/register/)
- [Student Dashboard](http://localhost:8000/dashboard/)

---

## 📦 Requirements

- Python 3.x
- pip
- PostgreSQL
- virtualenv

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/rseenikarthika/University-Course-Registration-System
cd University-Course-Registration-System
```

### 2. System Dependencies
```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv libpq-dev postgresql postgresql-contrib
```

---

## 🛢️ Database Setup (PostgreSQL)

```bash
sudo -u postgres psql
```

Inside PostgreSQL shell:
```sql
CREATE USER myuser WITH PASSWORD 'myuser';
CREATE DATABASE course_db OWNER myuser;
GRANT ALL PRIVILEGES ON DATABASE course_db TO myuser;
\c course_db
GRANT ALL ON SCHEMA public TO myuser;
\q
```

---

## 🐍 Python Environment

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

---

## 🏗️ Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## ▶️ Run the Server

```bash
python manage.py runserver
```

Visit the app at: [http://localhost:8000](http://localhost:8000)

---

## 👤 Default Superuser (Optional)

Create an admin user for Django admin panel:
```bash
python manage.py createsuperuser
```

Then visit: [http://localhost:8000/admin/](http://localhost:8000/admin/)

---

## 📂 Directory Structure (Important Files)

```
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register_student.html
│   ├── register_faculty.html
│   ├── course_register.html
│   └── dashboard.html
├── your_app/
│   ├── views.py
│   ├── models.py
│   └── urls.py
├── manage.py
└── requirements.txt
```

---

## 📝 License

MIT License

---

## 🙌 Credits

Developed by Seeni Karthika – ravikarthika2000@gmail.com
