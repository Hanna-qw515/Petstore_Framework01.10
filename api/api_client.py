# api_client.py
import requests


class PetstoreAPI:
    def __init__(self):
        self.base_url = 'https://petstore.swagger.io/v2'
        self.headers = {"Content-Type": "application/json"}

    def get_pet(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        return requests.get(url)

    def create_pet(self, payload):
        url = f'{self.base_url}/pet'
        return requests.post(url, json = payload, headers = self.headers)

    def update_pet(self, payload):
        url = f'{self.base_url}/pet'
        return requests.put(url, json = payload, headers = self.headers)

    def delete_pet(self, pet_id):
        url = f'{self.base_url}/pet/{pet_id}'
        return requests.delete(url, headers=self.headers)

    def find_pets_by_status(self, status):
        url = f'{self.base_url}/pet/findByStatus/{status}'
        return requests.get(url)




