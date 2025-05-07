from django.test import TestCase

from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Task

class TaskApiTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='evans', password='pass1234')
        self.client.force_authenticate(user=self.user)
        self.task = Task.objects.create(
            title = 'Sample task',
            description = 'Just testing',
            completed = False,
            owner = self.user

        )

        def test_get_tasks(self):
            url = reverse('task-list')
            response = self.client.get(url)
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(len(response.data['results']), 1)
            self.assertEqual(response.data['results']['title'], 'Sample Task')
