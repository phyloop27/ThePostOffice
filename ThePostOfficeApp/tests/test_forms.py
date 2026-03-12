from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import pytest
import pytest_cov # To run tests - pytest --cov=myproj tests/
import unit_test