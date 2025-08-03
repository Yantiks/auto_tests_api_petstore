from utils.api.helpers.base_url import HelperBaseUrl
import requests

class TestUser:
    def test_user(self, generate_client, set_headers):
        print(generate_client)
        response = requests.request("POST",f'{HelperBaseUrl.BASE_URL_ENV}/user', headers=set_headers, json=generate_client)
        print(response.status_code)
        print(response.json())