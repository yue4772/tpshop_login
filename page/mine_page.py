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
    # 收货地址
    address_button = By.XPATH, "//*[@text='收货地址']"

    @allure.step(title="点击登录/注册")
    def click_login_and_sign_up(self):
        self.click(self.login_and_sign_up_button)

    @allure.step(title="点击设置齿轮")
    def click_stting(self):
        self.click(self.stting_button)

    @allure.step(title="点击收获地址")
    def click_address(self):
        self.click(self.address_button)

    # 调用这个函数，就返回title bar的标题
    def get_title_bar_text(self):
        return  self.find_element(self.title_bar).text

    def is_login(self):
        return self.get_title_bar_text() == "设置"

    # 一边滑动一边找元素
    @allure.step(title="一边滑动一边找，点击收货地址")
    def click_address(self):
        self.scroll_find_element(self.address_button).click()

