import requests
import allure
import random
import string
import json
from data import Url, OrderTestData


@allure.step('Регистрируем нового курьера и возвращаем логин и пароль')
def create_new_courier_and_return_login_and_password():

    login_pass = {}

    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    response = requests.post(Url.BASE_URL+Url.CREATE_COURIER_HANDLE, data=payload)

    if response.status_code == 201:
        login_pass = {
            "login": login,
            "password": password,
            "firstName": first_name,
            "status_code": response.status_code,
            "json": response.json()
        }

    return login_pass


@allure.step('Генерируем рандомную строку')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Вход курьером')
def courier_login(login, password):
    payload = {
        'login': login,
        'password': password
    }
    response = requests.post(Url.BASE_URL+Url.LOGIN_COURIER_HANDLE, data=payload)
    return response


@allure.step('Удаление курьера')
def courier_delete(courier_id):
    response = requests.delete(f'{Url.BASE_URL}{Url.CREATE_COURIER_HANDLE}/{courier_id}')
    return response


@allure.step('Создание заказа')
def order_create(color):
    OrderTestData.ORDER['color'] = color
    payload = OrderTestData.ORDER
    response = requests.post(Url.BASE_URL+Url.ORDERS_HANDLE, data=json.dumps(payload))
    return response



