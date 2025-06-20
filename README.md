# CrudAPI

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-4.x-green.svg)](https://www.djangoproject.com/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)](https://crudapi-bwfv.onrender.com/swagger/)
[![Deployment](https://img.shields.io/badge/render-live-blue.svg)](https://crudapi-bwfv.onrender.com/swagger/)

A Django Rest Framework-based API for user registration, authentication, and task management 

 ## Live Demo
[Visit Swagger Docs] https://crudapi-bwfv.onrender.com/swagger/

 ## Features
* User registration and login (token-based authentication)
* Task CRUD operations
* User specific task filtering
* Fully documented with Swagger and ReDoc

 ## Tech Stack
- Django
- Django Rest Framework
- drf-yasg (Swagger documentation)
- SQLite (development database)
- Render (deployment platform
## Setup Instructions
1. *Clone the repository*

bash
  
git clone https://github.com/Ab494/crudapi.git

cd crudapi

2. *Create a virtual environment and activate it*

bash

python3 -m venv env

source env/bin/activate  # On Linux

env/scripts/activate  # On Windows

3. *Install dependencies*

   bash

   pip install requirements.txt

4. *Run migrations*

   bash

   python manage.py migrate

5. *Start the development server*

   bash

   python manage.py runserver

6. ## Access API Docs
   - Swagger: http://127.0.0.1:8000/swagger/
   - ReDoc: http://127.0.0.1:8000/redoc/

   ## Author
   ## Evans kipngeno cheruiyot

   LinkedIn: https://www.linkedin.com/in/evans-kipngeno-cheruiyot-448458346

## License
This project is licensed under the MIT License
   
