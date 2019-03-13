import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AdressInfoPage(BaseAction):

    name_edit_text = By.ID, "com.tpshop.malls:id/consignee_name_edtv"
    phone_edit_text = By.ID, "com.tpshop.malls:id/consignee_mobile_edtv"
    adress_edit_text = By.ID, "com.tpshop.malls:id/consignee_address_edtv"
    refion_button = By.ID, "com.tpshop.malls:id/consignee_region_txtv"

    @allure.step(title="输入收货人姓名")
    def input_name(self, text):
        self.input(self.name_edit_text, text)

    @allure.step(title="输入收货人手机号码")
    def input_phone(self, text):
        self.input(self.phone_edit_text, text)

    @allure.step(title="输入详细地址")
    def input_adress(self, text):
        self.input(self.adress_edit_text, text)

    @allure.step(title="点击所在地区")
    def click_refion(self):
        self.click(self.refion_button)