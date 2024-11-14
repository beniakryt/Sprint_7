import pytest
import requests
import allure  # Импортируем Allure
from data import ORDERS_URL, RESPONSE_STATUS, ORDER_DATA_1, ORDER_DATA_2, ORDER_DATA_3, ORDER_DATA_4


@pytest.mark.parametrize(
    'order_data, expected_status, expected_track_in_response',
    [
        (ORDER_DATA_1, RESPONSE_STATUS["created"], True),  # Один цвет: BLACK
        (ORDER_DATA_2, RESPONSE_STATUS["created"], True),  # Один цвет: GREY
        (ORDER_DATA_3, RESPONSE_STATUS["created"], True),  # Оба цвета
        (ORDER_DATA_4, RESPONSE_STATUS["created"], True),  # Цвет не указан
    ]
)
@allure.title("Тест создания заказа с разными цветами")
def test_create_order(order_data, expected_status, expected_track_in_response):
    with allure.step("Отправка запроса на создание заказа"):
        response = requests.post(ORDERS_URL, json=order_data)

    assert response.status_code == expected_status, f"Ожидался статус {expected_status}, но получили {response.status_code}"

    if expected_track_in_response:
        with allure.step("Проверка наличия track в ответе"):
            response_data = response.json()
            assert "track" in response_data, "В ответе отсутствует track"
