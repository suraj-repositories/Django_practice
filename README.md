
# 🐍 Python + Django Guide

<div align="center" style="display: flex; align-items: center; justify-content: center; gap: 20px; flex-wrap: wrap;">
  <img src="./images/icon.png" alt="Python Icon" width="100"/>
  <img src="./images/python.png" alt="Django Icon" width="100"/>
</div>

---

## ⚡ Essential Django Commands  

### 🔍 Check Django installation
```sh
python -m django --version
```

### 📂 Create a new project
```sh
django-admin startproject <project_name>
```

### ▶️ Start development server
```sh
python manage.py runserver
```

### 🗄️ Apply database migrations
```sh
python manage.py migrate
```

### 🏗️ Create a new app
```sh
python manage.py startapp <app_name>
```

### 🔄 Create & apply migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 🔑 Create superuser (Admin dashboard)
```sh
python manage.py createsuperuser
```

---

## 🐚 Django Shell (Database Access)

Django shell allows direct interaction with your database.  

Start the shell:
```sh
python manage.py shell
```

---

## 🌐 Django REST Implementations  

👉 [Django REST Example](https://github.com/suraj-repositories/Django_practice/blob/main/Django_05_rest_2/README.md)

---

## 🎨 Customizing Admin Dashboard  

### 🪛 Install **django-jazzmin**
```sh
pip install -U django-jazzmin
```

### 🛡 Add to `INSTALLED_APPS`
```python
INSTALLED_APPS = [
    "jazzmin",
    # other apps
]
```

### 🛠 Configure Settings (`settings.py`)  

#### Basic setup
```python
JAZZMIN_SETTINGS = {
    "site_title": "Rest API Admin",
    "show_ui_builder": True,
    # more options available in docs
}
```

#### UI Tweaks
```python
JAZZMIN_UI_TWEAKS = {
    "navbar_fixed": True,
    "footer_fixed": True,
    "sidebar_fixed": True,
    "theme": "sketchy",
    "brand_colour": "navbar-white",
    "accent": "accent-orange",
    "sidebar": "sidebar-light-orange",
    "button_classes": {
        "primary": "btn-outline-primary",
        "secondary": "btn-outline-secondary",
        "info": "btn-outline-info",
        "warning": "btn-outline-warning",
        "danger": "btn-outline-danger",
        "success": "btn-outline-success",
    },
}
```

🌍 Full docs → [Django Jazzmin Configuration](https://django-jazzmin.readthedocs.io/configuration/)  

---

## 🦚 Example Customized Dashboard  

<img src="./images/jazzmin-dashboard.png" alt="Jazzmin Dashboard Preview" width="600"/>

