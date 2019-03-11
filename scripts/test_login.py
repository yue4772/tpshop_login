import pytest

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page


class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize(("args"), analyze_file("login_data", "test_login"))
    def test_login(self,args):
        self.page.home.click_mine()
        self.page.mine.click_login_and_sign_up()
        self.page.login_and_sign_up.input_phone(args["phone"])
        self.page.login_and_sign_up.input_password(args["password"])
        self.page.login_and_sign_up.click_login()
        assert self.page.login_and_sign_up.is_login(args["expect"])


        # self.page.login_and_sign_up_page.input_phone(phone)
        # self.page.login_and_sign_up_page.input_password(password)
        # self.page.login_and_sign_up_page.click_login()
        # assert self.page.login_and_sign_up_page.is_login(expect)
