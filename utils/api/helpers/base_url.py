import requests
from utils.api.helpers.logger import log_request


class HelperBaseUrl:
    BASE_URL_ENV = 'https://petstore.swagger.io/v2'

    def init(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, path):
        url = self.base_url + path
        response = self.session.get(url)
        log_request(response)
        return response

