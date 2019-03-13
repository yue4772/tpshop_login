import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AdressListPage(BaseAction):

    new_adress_button = By.ID, "com.tpshop.malls:id/add_address_btn"

    @allure.step(title="点击新建地址")
    def click_new_adress(self):
        self.click(self.new_adress_button)