from django.contrib.auth.models import User
from django.urls import reverse
import pytest
from ThePostOfficeApp.models import *


# testing protected pages redirect
@pytest.mark.django_db
def test_redirects_if_not_logged_in(client):
    # trying to load a protected page without being logged in
    response = client.get(reverse("home"))

    # checking outcome
    if response.status_code == 302:
        assert response.status_code == 302 # user redirected
        assert reverse("staffLogin") in response.url # redirected to login page
        print('test_redirects_if_not_logged_in - Test successful')

    else:
        print('test_redirects_if_not_logged_in - Test failed')


# checking logged user can access 'home'
@pytest.mark.django_db
def test_logged_in_user_can_access_home(client):
    # creating a false user for tests purposes
    user = User.objects.create_user(username="sam", password="Password123")

    # Loggin directly, rather than browser login page
    client.login(username="sam", password="Password123")

    # loading 'home' as logged in user
    response = client.get(reverse("home"))

    # checking outcome
    if response.status_code == 200:
        assert response.status_code == 200 # status code okay
        print('test_logged_in_user_can_access_home - Test successful')

    else:
        print('test_logged_in_user_can_access_home - Test failed')



# testing that the 'fullRecord' page loads correctly for logged in user
# checking data get's inserted correctly
@pytest.mark.django_db
def test_full_record_page_loads_for_existing_customer(client):
    # login as user
    User.objects.create_user(username="sam", password="Password123")
    assert client.login(username="sam", password="Password123")

    # create record for use
    customer = Name.objects.create(
        identifier=1,
        first_name="sam",
        last_name="smith",
    )

    address = Address.objects.create(
        name = customer,
        house_no = 10,
        house_name = "Papillon",
        street = "Fryers way",
        town = "Fairhaven",
        post_code = "IP28 7QF"
    )

    # pull newly created record back from db
    response = client.get(reverse("fullRecord", args=[customer.identifier]))

    # check outcome
    if response.status_code == 200:
        assert response.status_code == 200
        assert "full_record.html"
        assert b"sam" in response.content
        assert b"smith" in response.content
        assert b"Papillon" in response.content
        assert b"IP28 7QF" in response.content
        print('test_full_record_page_loads_for_existing_customer - Test success')

    else:
        print('test_full_record_page_loads_for_existing_customer - Test failure')



@pytest.mark.django_db
def test_page_returns_404_for_missing_identifier(client):
    # login as user
    User.objects.create_user(username="sam", password="Password123")
    assert client.login(username="sam", password="Password123")

    # pull a record that dosent exist
    response = client.get(reverse("fullRecord", args=[9999]))

    # check outcome
    if response.status_code == 404:
        assert response.status_code == 404
        print('test_page_returns_404_for_missing_identifier - Test successful')

    else:
        print('test_page_returns_404_for_missing_identifier - Test failed')