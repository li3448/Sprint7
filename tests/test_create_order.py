import allure
import pytest
import helpers
from data import OrderTestData


@allure.story('Тест создания заказа')
class TestOrderCreating:
    @allure.title('Тест успешного создания заказа')
    @pytest.mark.parametrize('color', OrderTestData.SCOOTER_COLORS)
    def test_successful_order_creating(self, color):
        response = helpers.order_create(color)
        assert 'track' in response.text