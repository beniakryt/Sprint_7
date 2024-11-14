from data import BASE_URL, ORDERS_URL


class OrderMethods:

    def post_order(self, id, params):
        response = requests.post(f'{BASE_URL}{ORDERS_URL}finish/{id}', json=params)
        return response.status_code, response.model_damp(mode='json')
