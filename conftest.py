import pytest
from methods.order_methods import OrderMethods
from methods.courier_methods import CourierMethods
from data import COURIER_NAME

@pytest.fixture()
def order_methods():
    return OrderMethods()

@pytest.fixture()
def courier_methods():
    return CourierMethods()

@pytest.fixture()
def courier(courier_methods):
    response = courier_methods.create_courier(COURIER_NAME)
    courier_id = response.json().get('id')
    yield courier_id
    if courier_id:
        courier_methods.delete_courier(courier_id)
