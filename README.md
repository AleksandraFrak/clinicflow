# ClinicFlow

ClinicFlow is a Django web application for managing patients, doctors and medical appointments.

The project was created as part of an Object-Oriented Programming course and developed as a portfolio project.

---

## Features

- Patient management
  - create, read, update, delete
  - search patients by name, PESEL or email

- Doctor management
  - create, read, update, delete
  - specializations and room numbers

- Appointment management
  - create, read, update, delete
  - appointment status tracking
  - filter appointments by status

- Dashboard
  - total number of patients
  - total number of doctors
  - total number of appointments
  - upcoming appointments overview

- Admin panel
  - Django admin integration
  - searchable and filterable admin views

---

## Object-Oriented Programming concepts

This project uses object-oriented programming concepts such as:

- Django models as Python classes
- inheritance through an abstract `Person` base class
- model methods such as `__str__()` and `full_name()`
- relationships between objects using `ForeignKey`
- encapsulation of data structure in models
- reusable forms with `ModelForm`

---

## Tech Stack

- Python
- Django
- SQLite
- HTML
- CSS
- Git / GitHub

---

## Project Structure

```text
clinicflow/
├── clinic/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── admin.py
├── config/
│   ├── settings.py
│   └── urls.py
├── static/
│   └── css/
│       └── style.css
├── templates/
├── manage.py
├── requirements.txt
└── README.md
```

---
## Installation

Clone the repository:

```bash
git clone https://github.com/AleksandraFrak/clinicflow.git
cd clinicflow
```

Create and activate virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Create superuser:

```bash
python manage.py createsuperuser
```

Run development server:

```bash
python manage.py runserver
```

Open in browser:

```text
http://127.0.0.1:8000/
```

---

## Main pages

```text
/                  Dashboard
/patients/         Patient list
/doctors/          Doctor list
/appointments/     Appointment list
/admin/            Django admin panel
```

---

## Status

Project in development.

---

## Author

Aleksandra Frąk
Informatyka II stopień, I rok 
Katolicki Uniwerstet Lubelski