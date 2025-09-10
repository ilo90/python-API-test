import allure
import pytest

from config.base_test import BaseTest


@allure.epic('Basket tests')
@allure.feature('Basket API')
class TestBasketApi(BaseTest):

    @allure.title('Check basket items')
    def test_basket_api(self):
        response = self.basket_api.get_items_to_cart()

    @allure.title('Add item to basket')
    def test_update_basket(self):
        self.basket_api.post_update_basket(1)

    @allure.title('Update basket not exist item id')
    def test_update_basket_not_exist_id(self):
        self.basket_api.post_update_basket_not_exist_item_id()
