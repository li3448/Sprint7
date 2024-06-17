import pytest
import helpers


@pytest.fixture(scope='function')
def courier():
    courier = helpers.create_new_courier_and_return_login_and_password()
    courier_id = helpers.courier_login(courier['login'], courier['password']).json()['id']
    yield courier
    helpers.courier_delete(courier_id)