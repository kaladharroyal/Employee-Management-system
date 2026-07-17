# 🚀 Employee Management System

A production-ready **Employee Management System REST API** built with **Django** and **Django REST Framework**. The project provides secure authentication, employee and department management, email notifications, and email history tracking through a modular and scalable architecture.

---

## ✨ Features

- 🔐 Token-based Authentication
- 👥 Employee Management (CRUD)
- 🏢 Department Management (CRUD)
- 📧 SMTP Email Integration (Gmail)
- 📝 Email History & Logging
- 📄 RESTful API Architecture
- ⚡ Input Validation & Error Handling
- 📊 Pagination & Search Support
- 🛡️ Django Admin Dashboard
- ☁️ Deployment Ready (Render + Gunicorn)

---

# 📸 Project Architecture

```
Employee-Management-System/
│
├── authentication/          # User authentication
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── employee/                # Employee Management
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── department/              # Department Management
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── email_service/           # Email Sending
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── history/                 # Email History
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── .env.example
└── README.md
```

---

# 🛠️ Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.x |
| Framework | Django 5.x |
| API | Django REST Framework |
| Database | PostgreSQL (Supabase) |
| Authentication | DRF Token Authentication |
| Email | Gmail SMTP |
| Deployment | Gunicorn + Render |
| Version Control | Git & GitHub |

---

# ⚙️ System Workflow

```
                Client
                  │
                  ▼
          Django URL Router
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
Authentication Employee Department
     │            │            │
     └──────┬─────┴────────────┘
            ▼
      Email Service
            │
            ▼
       Email History
            │
            ▼
       PostgreSQL Database
```

---

# 🚀 Getting Started

## Prerequisites

- Python 3.10+
- PostgreSQL
- Git
- Virtual Environment

---

## 1. Clone Repository

```bash
git clone https://github.com/prudviraj12345/Employee-Management-system.git

cd Employee-Management-system
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Configure Environment Variables

Create a `.env` file.

```env
# Django
SECRET_KEY=your-secret-key
DEBUG=True

ALLOWED_HOSTS=localhost,127.0.0.1

# Database
DATABASE_URL=postgresql://username:password@host:port/database

# Email
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
DEFAULT_FROM_EMAIL=your-email@gmail.com
```

---

## 5. Apply Migrations

```bash
python manage.py makemigrations

python manage.py migrate
```

---

## 6. Create Superuser

```bash
python manage.py createsuperuser
```

---

## 7. Run Server

```bash
python manage.py runserver
```

Open

```
http://127.0.0.1:8000/
```

---

# 🔑 API Endpoints

## Authentication

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/login/` | Login |
| GET | `/api/profile/` | User Profile |
| PUT | `/api/profile/` | Update Profile |
| PATCH | `/api/profile/` | Partial Update |
| POST | `/api/change-password/` | Change Password |
| GET | `/api/stats/` | Public Statistics |

---

## Departments

| Method | Endpoint |
|---------|----------|
| GET | `/api/departments/` |
| POST | `/api/departments/` |
| GET | `/api/departments/{id}/` |
| PUT | `/api/departments/{id}/` |
| DELETE | `/api/departments/{id}/` |

---

## Employees

| Method | Endpoint |
|---------|----------|
| GET | `/api/employees/` |
| POST | `/api/employees/` |
| GET | `/api/employees/{id}/` |
| PUT | `/api/employees/{id}/` |
| DELETE | `/api/employees/{id}/` |

---

## Email Service

| Method | Endpoint |
|---------|----------|
| GET | `/api/emails/` |
| POST | `/api/emails/` |
| GET | `/api/emails/{id}/` |
| PUT | `/api/emails/{id}/` |
| DELETE | `/api/emails/{id}/` |

---

## Email History

| Method | Endpoint |
|---------|----------|
| GET | `/api/history/` |

---

# 📧 Email Flow

```
Create Employee
       │
       ▼
Create Email Request
       │
       ▼
SMTP Service
       │
       ▼
Email Sent
       │
       ▼
Save Email Log
       │
       ▼
History Table
```

---

# 🔐 Authentication

The API uses **Token Authentication**.

Example:

```http
Authorization: Token your_token_here
```

---

# 📂 Environment Variables

| Variable | Description |
|-----------|-------------|
| SECRET_KEY | Django Secret Key |
| DEBUG | Debug Mode |
| DATABASE_URL | PostgreSQL Connection URL |
| EMAIL_HOST | SMTP Host |
| EMAIL_PORT | SMTP Port |
| EMAIL_USE_TLS | TLS Enable |
| EMAIL_HOST_USER | Gmail Address |
| EMAIL_HOST_PASSWORD | Gmail App Password |
| DEFAULT_FROM_EMAIL | Sender Email |

---

# 🛡️ Validation

The application validates:

- Employee Email Uniqueness
- Employee ID Format
- Phone Number Format
- Department References
- Required Fields
- Authentication Tokens

---

# 📊 Built-in Features

- Token Authentication
- CRUD Operations
- Modular Django Apps
- Email Retry Mechanism
- Email Logging
- Pagination
- Filtering
- Search
- Error Handling
- Admin Dashboard

---

# 🖥️ Django Admin

Access the admin dashboard:

```
http://127.0.0.1:8000/admin/
```

Using your superuser credentials you can:

- Manage Employees
- Manage Departments
- View Users
- Track Emails
- Monitor History

---

# ☁️ Deployment

The project is deployment-ready for:

- Render
- Railway
- DigitalOcean
- AWS EC2
- Azure
- Heroku (with minor changes)

Production stack:

- Gunicorn
- PostgreSQL
- Environment Variables
- Static Files Support

---

# 🧪 Running Tests

```bash
python manage.py test
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository

2. Create a new branch

```bash
git checkout -b feature/your-feature
```

3. Commit your changes

```bash
git commit -m "Add your feature"
```

4. Push to GitHub

```bash
git push origin feature/your-feature
```

5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests where applicable.

---

# 🐛 Reporting Issues

Found a bug or have a feature request?

Please open an issue describing:

- Problem
- Expected behavior
- Steps to reproduce
- Environment information

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Prudhvi Raj**

GitHub: https://github.com/prudviraj12345

---

## ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork the project
- 🐛 Report bugs
- 💡 Suggest improvements
- 🤝 Submit Pull Requests

Every contribution helps improve the project.
