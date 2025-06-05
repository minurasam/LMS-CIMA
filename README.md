# LMS-CIMA

An E-Learning Platform tailored for CIMA (Chartered Institute of Management Accountants) students, built with Django, Bootstrap, and Font Awesome, and deployed on Heroku.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Application](#running-the-application)
- [Deployment](#deployment)
- [Project Structure](#project-structure)
  - [Admin App](#admin-app)
  - [elearningDash App](#elearningdash-app)
  - [Static & Media Files](#static--media-files)
  - [Other Key Files](#other-key-files)
- [Contributing](#contributing)
- [License](#license)
- [Authors & Acknowledgements](#authors--acknowledgements)

---

## Project Overview

LMS-CIMA is a web-based Learning Management System designed specifically for CIMA students. Administrators can create, manage, and monitor courses, quizzes, and resources, while students access study materials, track progress, and take assessments. The backend is built with Django (Python), and the frontend uses Bootstrap and Font Awesome. The application is ready for deployment on Heroku.

---

## Features

- **User Authentication & Roles**
  - Student registration and login
  - Administrator login with elevated privileges

- **Course Management (Admin)**
  - Create, read, update, and delete (CRUD) courses
  - Upload lecture materials (PDFs, videos)
  - Organize content into modules or lessons

- **Quiz & Assessment**
  - Admin can create quizzes (multiple-choice, true/false)
  - Students attempt quizzes and view immediate feedback
  - Automatic scoring and progress tracking

- **Dashboard (Student)**
  - Overview of enrolled courses
  - Progress bars for each course/module
  - Display of upcoming assignments and quiz deadlines

- **Static & Media Handling**
  - Serve CSS/JS via the `static/` directory
  - Store uploaded images, PDFs, and video files in `media/`

- **Responsive Front-End**
  - Built with Bootstrap for mobile-friendly layout
  - Font Awesome icons for visual cues

- **Deployment-Ready**
  - `Procfile` and `runtime.txt` included for Heroku
  - `requirements.txt` lists all Python dependencies

---

## Technologies Used

- **Backend**  
  - Python 3.x  
  - Django 3.x (or higher)

- **Frontend**  
  - Bootstrap 4 (or 5)  
  - Font Awesome  
  - HTML5 & CSS3  
  - JavaScript (vanilla for small interactivity)

- **Database**  
  - SQLite (default for development)  
  - PostgreSQL (recommended for production/Heroku)

- **Hosting & Deployment**  
  - Heroku (Procfile, `runtime.txt`, Gunicorn)

- **Version Control**  
  - Git & GitHub

---

## Prerequisites

Before getting started, ensure that you have the following installed on your development machine:

1. **Python 3.x**  
2. **pip** (Python package installer)  
3. (Optional but recommended) **virtualenv** or **venv** for creating isolated Python environments  
4. **Git** (for cloning the repository)

---

## Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/minurasam/LMS-CIMA.git
   cd LMS-CIMA
   ```

2. **Create & activate a virtual environment**  
   - Using `venv` (Python 3 built-in):  
     ```bash
     python3 -m venv venv
     source venv/bin/activate   # macOS/Linux
     venv\Scripts\activate      # Windows
     ```

3. **Install Python dependencies**  
   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Apply database migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (Admin)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files (for production)**  
   ```bash
   python manage.py collectstatic
   ```

---

## Configuration

1. **Environment Variables**  
   Create a `.env` file (or set environment variables directly) with the following keys:
   ```env
   SECRET_KEY=your-django-secret-key
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1,<your-heroku-app-name>.herokuapp.com
   DATABASE_URL=postgres://user:password@hostname:port/dbname
   ```

2. **`settings.py` Adjustments**  
   Ensure that `settings.py` reads from environment variables. Example snippet:
   ```python
   import os
   from dotenv import load_dotenv

   load_dotenv()

   SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret-key")
   DEBUG = os.getenv("DEBUG", "False") == "True"
   ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",")

   STATIC_URL = '/static/'
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

   MEDIA_URL = '/media/'
   MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
   ```

---

## Running the Application

1. **Start the Development Server**  
   ```bash
   python manage.py runserver
   ```

2. **Access the Admin Interface**  
   - `http://127.0.0.1:8000/admin/`

3. **Access the Student Dashboard**  
   - `http://127.0.0.1:8000/`

4. **Creating Content**  
   Use the admin panel to create Courses, Modules, and Quizzes.

---

## Deployment

[... truncated for brevity in this explanation, but full content continues in the file below ...]
