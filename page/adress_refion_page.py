import random

import time

import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction


class AdressRefionPage(BaseAction):

    city_feature = By.ID, "com.tpshop.malls:id/tv_city"
    commit_button = By.ID, "com.tpshop.malls:id/btn_right"

    @allure.step(title='收货人地址区域 - 选择区域')
    def click_city(self):

        for _ in range(4):
            city_list = self.find_elements(self.city_feature)
            city_count = len(city_list)
            city_index = random.randint(0, city_count - 1)
            city_list[city_index].click()
            time.sleep(2)

    @allure.step(title='收货人地址区域 - 点击确定')
    def click_commit(self):
        self.click(self.commit_button)

