import random

import allure
import pytest
import time

from base.base_analyze import analyze_file
from base.base_driver import init_driver
from page.page import Page

# 随机密码函数
def random_password():
    password=''
    for i in range(8):
        password += str(random.randint(0,9))
    return password



class TestLogin:

    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    # @pytest.mark.parametrize(("args"), analyze_file("login_data", "test_login"))
    # def test_login(self,args):
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_sign_up()
    #     self.page.login_and_sign_up.input_phone(args["phone"])
    #     self.page.login_and_sign_up.input_password(args["password"])
    #     self.page.login_and_sign_up.click_login()
    #     assert self.page.login_and_sign_up.is_login_seccess(args["expect"])
    #
    # @pytest.mark.parametrize(("args"), analyze_file("login_data", "test_login_miss_part"))
    # def test_login_miss_part(self, args):
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_sign_up()
    #     self.page.login_and_sign_up.input_phone(args["phone"])
    #     self.page.login_and_sign_up.input_password(args["password"])
    #     # 定位登录按钮是否可用、
    #     assert  not self.page.login_and_sign_up.is_login_enable()
    #
    #
    # @pytest.mark.parametrize("password",[random_password(), random_password()])
    # def test_show_passwod(self, password):
    #     self.page.home.click_mine()
    #     self.page.mine.click_login_and_sign_up()
    #     self.page.login_and_sign_up.input_password(password)
    #     # 判断密码找不到
    #     assert not self.page.login_and_sign_up.is_passwod_exist(password)
    #     # 点击显示密码按钮
    #     self.page.login_and_sign_up.click_show_password()
    #     time.sleep(1)
    #     allure.attach("截图", self.driver.get_screenshot_as_png(), allure.attach_type.PNG)
    #     # 判断密码找到，找到就成功
    #     assert self.page.login_and_sign_up.is_passwod_exist(password)





