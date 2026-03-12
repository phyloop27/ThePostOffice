from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
import pytest
import pytest_cov # To run tests - pytest --cov=myproj tests/
import unit_test

# @pytest.mark.django_db - telling pytest the tests needs database access
# client - django’s tests client it simulate's browser requests.
# reverse -builds the URL from the URL name always better than hardcoding strings

# Running only tests from this file:
# pytest tests/test_auth.py


def test_login_page_loads(client):
    response = client.get(reverse("staffLogin"))

    # checking outcome
    if response.status_code == 200:
        assert response.status_code == 200 # status code okay
        assert b"Local Post Office Login" in response.content
        print('Test successful')

    else:
        print('Test failed')


@pytest.mark.django_db
def test_valid_user_log_in(client):
    # create user for tests
    User.objects.create_user(username="sam", password="Password123")

    # using 'client()' to log directly with the request info
    response = client.post(reverse("staffLogin"), {
        "username": "sam",
        "password": "Password123"})

    # checking outcome
    if response.status_code == 302:
        assert response.status_code == 302 # resource has been temporarily moved or user being relocated
        assert response.url == reverse("home")
        print('test_valid_user_log_in - Test successful')

    else:
        print('test_valid_user_log_in - Test failed')


@pytest.mark.django_db
def test_invalid_login_error(client):
    # create user for tests
    User.objects.create_user(username="sam", password="Password123")

    # using 'client()' to log directly with the request info
    response = client.post(reverse("staffLogin"), {
        "username": "sam",
        "password": "Password456"}) # insert wrong password

    # checking outcome
    if response.status_code == 200:
        assert response.status_code == 200 # status code okay
        assert b"Invalid Credentials" in response.content
        print('test_invalid_login_error - Test successful')

    else:
        print('test_invalid_login_error - Test failed')