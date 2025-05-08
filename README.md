# CrudAPI
A Django Rest Framework-based API for user registration, authentication and task management.

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

  *bash
  
*git clone https://github.com/Ab494/crudapi.git

   *cd crudapi
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

   LinkedIn: https:www.linkein.com/in/evans-cheruiyot-448458346

## License
This project is licensed under the MIT License
   
