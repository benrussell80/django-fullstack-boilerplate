from django.test import TestCase
from . import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

User = get_user_model()

# Create your tests here.
class BaseTestCase(TestCase):
    def setUp(self):
        pass