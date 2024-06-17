import allure
import helpers
from data import Messages
from conftest import courier

@allure.story('Тесты на вход курьера')
class TestCourierLogin:
    @allure.title('Тест успешного входа')
    def test_successful_courier_login(self, courier):
        response = helpers.courier_login(courier['login'], courier['password'])
        assert response.status_code == 200 and 'id' in response.text, \
            f'Status code: {response.status_code}, Response: {response.text}'

    @allure.title('Вход с незаполненным полем "login"')
    def test_courier_login_no_login(self, courier):
        response = helpers.courier_login('', courier['password'])
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Вход с незаполненным полем "password"')
    def test_courier_login_no_password(self, courier):
        response = helpers.courier_login(courier['login'], '')
        assert response.status_code == 400 and response.json()['message'] == Messages.LOGIN_BAD_REQUEST_400, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Вход с неверно заполненным полем "login"')
    def test_courier_login_wrong_login(self, courier):
        response = helpers.courier_login(courier['password'], courier['password'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"

    @allure.title('Тест входа с неверно заполненным полем "password"')
    def test_courier_login_wrong_password(self, courier):
        response = helpers.courier_login(courier['login'], courier['login'])
        assert response.status_code == 404 and response.json()['message'] == Messages.LOGIN_NOT_FOUND_404, \
            f"Status code: {response.status_code}, Response message: {response.json()}"