import allure
import pytest
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class MinePage(BaseAction):
    # 登录/注册
    login_and_sign_up_button = By.XPATH, "//*[@text='登录/注册']"
    # 设置齿轮
    stting_button = By.ID, "com.tpshop.malls:id/setting_btn"
    # 标题
    title_bar = By.ID, "com.tpshop.malls:id/titlebar_title_txtv"

    @allure.step(title="点击登录/注册")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)

    @allure.step(title="点击设置齿轮")
    def click_stting_button(self):
        self.click(self.stting_button)

    # 调用这个函数，就返回title bar的标题
    def get_title_bar_text(self):
        return  self.find_element(self.title_bar).text
