import pytest
from faker import Faker
from test_data.models import Pet, Category, Tag
from test_data.models import User
from typing import Optional, List, Dict


@pytest.fixture
def generate_client():
    fake = Faker("ru_RU")
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
        "Accept": "application/json",
    }

@pytest.fixture
def generate_pet():
    fake = Faker("en_US")

    # приватная функция, которая создает данные для модели Pet. Изолирует логику генерации от внешнего кода
    def _generate_pet(
            pet_id: Optional[int] = None,
            status: Optional[str] = "available",
            min_photos: int = 1,
            min_tags: int = 1
    ) -> dict:
        """Генератор тестовых данных для Pet.

        Args:
            pet_id: Если None - сгенерируется случайный
            status: Один из ['available', 'pending', 'sold']
            min_photos: Минимальное количество фото
            min_tags: Минимальное количество тегов
        """
        # Генерация категории
        category = {
            "id": fake.unique.random_int(min=1, max=1000),
            "name": fake.word().capitalize() + " Category"
        }

        # Генерация тегов
        tags = [
            {
                "id": fake.unique.random_int(min=1, max=1000),
                "name": fake.word().capitalize() + " Tag"
            }
            for _ in range(fake.random_int(min=min_tags, max=3))
        ]

        # Генерация фото
        photo_urls = [
            f"https://{fake.domain_name()}/photos/{fake.uuid4()}.jpg"
            for _ in range(fake.random_int(min=min_photos, max=5))
        ]

        return {
            "id": pet_id if pet_id is not None else fake.unique.random_int(min=1, max=10 ** 6),
            "category": category,
            "name": fake.first_name() + " the " + fake.color_name().capitalize(),
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status
        }

    return _generate_pet