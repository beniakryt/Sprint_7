import pytest
import requests
import random
import string
import allure  # Импортируем Allure
from data import COURIERS_URL
from methods.courier_methods import CourierMethods

@pytest.fixture
def courier_methods():
    return CourierMethods()

def generate_unique_courier_data():
    return {
        "login": ''.join(random.choices(string.ascii_lowercase, k=10)),
        "password": ''.join(random.choices(string.ascii_lowercase, k=10)),
        "firstName": "CourierTest"
    }

@allure.title("Test to create a courier successfully")
def test_create_courier_success(courier_methods):
    unique_courier_data = generate_unique_courier_data()
    with allure.step("Create a new courier"):
        response = requests.post(COURIERS_URL, json=unique_courier_data)
    assert response.status_code == 201

@allure.title("Test to create a duplicate courier")
def test_create_duplicate_courier(courier_methods):
    first_courier = courier_methods.register_new_courier_and_return_login_password()
    duplicate_courier = {
        "login": first_courier["login"],
        "password": first_courier["password"],
        "firstName": first_courier["firstName"]
    }
    with allure.step("Attempt to create duplicate courier"):
        response = requests.post(COURIERS_URL, json=duplicate_courier)
    assert response.status_code == 409

@allure.title("Test to create a courier with missing fields")
def test_create_courier_missing_fields(courier_methods):
    incomplete_data = {
        "login": "testlogin"
    }
    with allure.step("Attempt to create courier with missing fields"):
        response = requests.post(COURIERS_URL, json=incomplete_data)
    assert response.status_code == 400

@allure.title("Test to create a courier and check the response code")
def test_create_courier_response_code(courier_methods):
    unique_courier_data = generate_unique_courier_data()
    with allure.step("Create a new courier and check response code"):
        response = requests.post(COURIERS_URL, json=unique_courier_data)
    assert response.status_code == 201

@allure.title("Test that the response includes 'ok' key")
def test_create_courier_response_ok(courier_methods):
    unique_courier_data = generate_unique_courier_data()
    with allure.step("Create a new courier and verify response includes 'ok' key"):
        response = requests.post(COURIERS_URL, json=unique_courier_data)
    assert response.status_code == 201
    assert response.json().get("ok") == True

@allure.title("Test to create a courier with existing login")
def test_create_courier_existing_login(courier_methods):
    first_courier = courier_methods.register_new_courier_and_return_login_password()
    duplicate_data = {
        "login": first_courier["login"],
        "password": "new_password",
        "firstName": "NewCourier"
    }
    with allure.step("Attempt to create courier with existing login"):
        response = requests.post(COURIERS_URL, json=duplicate_data)
    assert response.status_code == 409
