import requests
from utils.api.helpers.base_url import HelperBaseUrl
from test_data.models import Pet, Category, Tag

class TestPet:
    def test_add_a_pet(self, generate_pet, set_headers):
        # Генерируем данные питомца
        pet_data = generate_pet()
        print(pet_data)

        # Отправляем запрос
        response = requests.post(
            f'{HelperBaseUrl.BASE_URL_ENV}/pet',
            headers=set_headers,
            json=pet_data
        )

        print(response.json())
        # Проверяем ответ
        assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"

        # Парсим ответ через Pydantic
        response_data = response.json()
        created_pet = Pet(**response_data)

        # Проверяем данные
        assert created_pet.id == pet_data["id"]
        assert created_pet.name == pet_data["name"]
        assert created_pet.status == pet_data["status"]

        # Дополнительные проверки
        assert len(created_pet.photoUrls) >= 1
        assert created_pet.tags[0].id > 0

