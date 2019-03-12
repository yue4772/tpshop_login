import allure
import pytest
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class LoginandsignupPage(BaseAction):
    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"
    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"
    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    @allure.step(title="输入电话号码")
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    @allure.step(title="输入密码")
    def input_password(self, text):
        self.input(self.password_edit_text, text)

    @allure.step(title="点击登录")
    def click_login(self):
        self.click(self.login_button)


    def is_login(self, content):
        try:
            self.find_toast(content)
            return True
        except Exception:
            return False

