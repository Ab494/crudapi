from django.apps import AppConfig
from django.contrib.auth import get_user_model
from django.db.utils import OperationalError
import logging


class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
    def ready(self):
        try:
            User = get_user_model()
            
            if not User.objects.filter(username="admin").exists():
                User.objects.create_superuser(
                
                username = 'admin',
                email = 'cheruiyotevans646@gmail.com',
                password = 'Gaapgx89'

            )
            logging.info("Superuser 'admin' created.")
        except OperationalError:
            pass
