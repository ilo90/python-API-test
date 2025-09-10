from config.base_test import BaseTest


class TestRoles(BaseTest):

    def test_roles_api(self):
        self.roles_api.get_roles()
