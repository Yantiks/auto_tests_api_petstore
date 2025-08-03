import pytest
from faker import Faker

from test_data.models import BaseUser


@pytest.fixture
def generate_client():
    fake = Faker("ru_RU")
    # base_user = User()
    return {
        "id": fake.postcode(),
        "username": fake.user_name(),
        "firstName": fake.first_name(),
        "lastName": fake.last_name(),
        "email": fake.email(),
        "password": fake.password(),
        "phone": fake.phone_number(),
        "userStatus": 0
    }

@pytest.fixture
def set_headers():
    return {
        "Content-Type": "application/json",
    }
