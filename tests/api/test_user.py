from test_data.models import User
from utils.api.helpers.base_url import HelperBaseUrl
import requests
from pydantic import ValidationError

class TestUser:
    def test_user(self, generate_client, set_headers):
        print(generate_client)
        response = requests.request("POST",f'{HelperBaseUrl.BASE_URL_ENV}/user', headers=set_headers, json=generate_client)

        user_data = response.json()
        try:
            user = User(**user_data) #распаковка словаря в параметры модели
        except ValidationError as e:
            print(f"Validation Error: {e}")

        assert user.code == 200, f"Получен код {user.code}, а должен быть 200"

