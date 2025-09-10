from services.basket_service.basket.api_basket import BasketApi
from services.identity_service.roles.api_roles import RolesApi


class BaseTest:

    def setup_method(self):
        self.basket_api = BasketApi()
        self.roles_api = RolesApi()

