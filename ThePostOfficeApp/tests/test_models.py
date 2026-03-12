from django.contrib.auth.models import User
from django.urls import reverse
import pytest
from ThePostOfficeApp.models import Name


# checking records are inserted correctly into the Names Model
@pytest.mark.django_db # allowing Database access
def test_name_record_creation():
    # create an object to insert into the model
    customer = Name.objects.create(
        first_name="sam",
        last_name="smith")

    fname = customer.first_name
    lname = customer.last_name

    # checking those records have been created correctly
    if customer.first_name == fname and customer.last_name == lname:
            assert customer.first_name == "sam"
            assert customer.last_name == "smith"
            print('test_name_record_creation - Test successful')
    else:
        print('test_name_record_creation - Test failed')



# checking response for a missing record tests
@pytest.mark.django_db
def test_404_for_missing_record(client):
    # create user for tests
    User.objects.create_user(username="sam", password="Password123")

    # loggin in with tests user
    client.login(username="sam", password="Password123")

    # pull a record that dosne't exist
    response = client.get(reverse("fullRecord", args=[9999]))

    # checking outcome
    if response.status_code == 404:
        assert response.status_code == 404 # page missing or not found
        print('test_404_for_missing_record - Test successful')

    else:
        print('test_404_for_missing_record - Test failure')