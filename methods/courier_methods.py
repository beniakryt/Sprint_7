import requests
import random
import string
from data import COURIERS_URL

class CourierMethods:
    def generate_random_string(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    def register_new_courier_and_return_login_password(self):
        login = self.generate_random_string(10)
        password = self.generate_random_string(10)
        first_name = self.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        response = requests.post(COURIERS_URL, json=payload)

        if response.status_code == 201:
            return {"login": login, "password": password, "firstName": first_name}
        return {}
