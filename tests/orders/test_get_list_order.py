import requests
import allure  # Импортируем Allure
from data import ORDERS_URL, RESPONSE_STATUS


@allure.title("Тест получения списка заказов для курьера с указанным ID")
def test_get_orders_with_courier_id():

    courier_id = 423976
    orders_url = f"{ORDERS_URL}?courierId={courier_id}&page=0&limit=2"

    with allure.step("Отправка запроса для получения списка заказов"):
        response = requests.get(orders_url)

    assert response.status_code == RESPONSE_STATUS["ok"], f"Ожидался статус {RESPONSE_STATUS['ok']}, но получили {response.status_code}"

    with allure.step("Проверка, что в ответе содержится ключ 'orders'"):
        response_data = response.json()
        assert "orders" in response_data, "'orders' ключ отсутствует в ответе"

    with allure.step("Проверка, что 'orders' это список"):
        assert isinstance(response_data["orders"], list), "'orders' должно быть списком"
