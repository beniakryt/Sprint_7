import pytest
import random
import string
import requests
from unittest.mock import patch
import allure  # Импортируем Allure
from data import COURIERS_URL, ERROR_MESSAGES, RESPONSE_STATUS

def generate_unique_courier_data():
    return {
        "login": ''.join(random.choices(string.ascii_lowercase + string.digits, k=10)),
        "password": "password123",
        "firstName": "CourierTest"
    }

@pytest.fixture
def unique_courier_data():
    return generate_unique_courier_data()

@allure.title("Test courier can successfully log in")
def test_courier_can_login(unique_courier_data):
    with allure.step("Register the courier"):
        response = requests.post(COURIERS_URL, json=unique_courier_data)
        assert response.status_code == RESPONSE_STATUS["created"]

    with allure.step("Log in with courier credentials"):
        login_url = f"{COURIERS_URL}login"
        login_data = {
            "login": unique_courier_data["login"],
            "password": unique_courier_data["password"]
        }
        response = requests.post(login_url, json=login_data)
        assert response.status_code == RESPONSE_STATUS["ok"]

@allure.title("Test login requires all fields (login and password)")
def test_login_requires_all_fields(unique_courier_data):
    login_data = {
        "login": unique_courier_data["login"]
    }
    login_url = f"{COURIERS_URL}login"

    with allure.step("Attempt to log in without password"):
        with patch("requests.post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.status_code = RESPONSE_STATUS["bad_request"]
            mock_response.json.return_value = {"message": ERROR_MESSAGES["missing_password"]}

            response = requests.post(login_url, json=login_data)
            assert response.status_code == RESPONSE_STATUS["bad_request"]

@allure.title("Test invalid login or password")
def test_invalid_login_or_password(unique_courier_data):
    invalid_login_data = {
        "login": "wrong_login",
        "password": unique_courier_data["password"]
    }
    login_url = f"{COURIERS_URL}login"
    with allure.step("Attempt login with wrong login"):
        response = requests.post(login_url, json=invalid_login_data)
        assert response.status_code == RESPONSE_STATUS["not_found"]

    invalid_password_data = {
        "login": unique_courier_data["login"],
        "password": "wrong_password"
    }
    with allure.step("Attempt login with wrong password"):
        response = requests.post(login_url, json=invalid_password_data)
        assert response.status_code == RESPONSE_STATUS["not_found"]

@allure.title("Test missing field in login request")
def test_missing_field_in_login_request(unique_courier_data):
    incomplete_data = {
        "login": unique_courier_data["login"]
    }
    login_url = f"{COURIERS_URL}login"

    with allure.step("Attempt to log in with missing password"):
        with patch("requests.post") as mock_post:
            mock_response = mock_post.return_value
            mock_response.status_code = RESPONSE_STATUS["bad_request"]
            mock_response.json.return_value = {"message": ERROR_MESSAGES["missing_password"]}

            response = requests.post(login_url, json=incomplete_data)
            assert response.status_code == RESPONSE_STATUS["bad_request"]

@allure.title("Test login for non-existent user")
def test_login_for_non_existent_user(unique_courier_data):
    login_data = {
        "login": "non_existent_user",
        "password": "somepassword"
    }
    login_url = f"{COURIERS_URL}login"
    with allure.step("Attempt login with a non-existent user"):
        response = requests.post(login_url, json=login_data)
        assert response.status_code == RESPONSE_STATUS["not_found"]
        response_data = response.json()
        assert response_data["message"] == ERROR_MESSAGES["account_not_found"]

@allure.title("Test successful login returns user id")
def test_successful_login_returns_id():
    unique_courier_data = generate_unique_courier_data()
    with allure.step("Register new courier"):
        response = requests.post(COURIERS_URL, json=unique_courier_data)
        assert response.status_code == RESPONSE_STATUS["created"]

    login_url = f"{COURIERS_URL}login"
    login_data = {
        "login": unique_courier_data["login"],
        "password": unique_courier_data["password"]
    }
    with allure.step("Login with registered courier"):
        response = requests.post(login_url, json=login_data)
        assert response.status_code == RESPONSE_STATUS["ok"]

    with allure.step("Check if id is present in the response"):
        response_data = response.json()
        assert "id" in response_data
