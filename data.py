BASE_URL = 'https://qa-scooter.praktikum-services.ru/api/v1/'
ORDERS_URL = f"{BASE_URL}orders/"
COURIERS_URL = f"{BASE_URL}courier/"

ORDER_DATA_1 = {
    "firstName": "Naruto",
    "lastName": "Uchiha",
    "address": "Konoha, 142 apt.",
    "metroStation": "4",
    "phone": "+7 800 355 35 35",
    "rentTime": 5,
    "deliveryDate": "2020-06-06",
    "comment": "Saske, come back to Konoha",
    "color": ["BLACK"]
}

ORDER_DATA_2 = {
    "firstName": "Saske",
    "lastName": "Uchiha",
    "address": "Konoha, 101 apt.",
    "metroStation": "1",
    "phone": "+7 800 355 35 36",
    "rentTime": 3,
    "deliveryDate": "2020-06-07",
    "comment": "Urgent, please",
    "color": ["GREY"]
}

ORDER_DATA_3 = {
    "firstName": "Hinata",
    "lastName": "Hyuga",
    "address": "Konoha, 222 apt.",
    "metroStation": "5",
    "phone": "+7 800 355 35 37",
    "rentTime": 7,
    "deliveryDate": "2020-06-08",
    "comment": "Deliver with care",
    "color": ["BLACK", "GREY"]
}

ORDER_DATA_4 = {
    "firstName": "Kiba",
    "lastName": "Inuzuka",
    "address": "Konoha, 150 apt.",
    "metroStation": "3",
    "phone": "+7 800 355 35 38",
    "rentTime": 4,
    "deliveryDate": "2020-06-09",
    "comment": "No color preference",
    "color": []
}

COURIER_NAME = "unique_courier_name"
COURIER_DATA = {
    "login": "test_courier_login",
    "password": "test_courier_password",
    "firstName": "CourierFirstName"
}
#выбор цвета
COLOR_OPTIONS = ["BLACK", "GREY"]

ERROR_MESSAGES = {
    "missing_password": "Недостаточно данных для входа",
    "invalid_login_or_password": "Учетная запись не найдена",
    "insufficient_data_for_creation": "Недостаточно данных для создания учетной записи",
    "account_not_found": "Учетная запись не найдена"
}

RESPONSE_STATUS = {
    "created": 201,
    "ok": 200,
    "bad_request": 400,
    "not_found": 404
}
