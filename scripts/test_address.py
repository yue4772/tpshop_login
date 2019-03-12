from base.base_driver import init_driver
from page.page import Page


class TestAddress:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    def test_address(self):
        self.page.home.click_mine()
        self.page.mine.click_stting_button()
        # 判断是否登录
        if not self.page.mine.get_title_bar_text():
            # 登录
            self.page.login_and_sign_up.input_phone("13800138006")
            self.page.login_and_sign_up.input_password("123456")
            self.page.login_and_sign_up.click_login()
            # 根据toast判断是否登录成功
            assert self.page.login_and_sign_up.is_login()
        # 点击收货地址


