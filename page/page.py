from page.adress_info_page import AdressInfoPage
from page.adress_refion_page import AdressRefionPage
from page.adresss_list_page import AdressListPage
from page.home_page import HomePage
from page.login_and_sign_up_page import LoginandsignupPage
from page.mine_page import MinePage


class Page:
    def __init__(self, driver):
        self.driver = driver

    @property
    def home(self):
        return HomePage(self.driver)

    @property
    def mine(self):
        return MinePage(self.driver)

    @property
    def login_and_sign_up(self):
        return LoginandsignupPage(self.driver)

    @property
    def adress_list(self):
        return AdressListPage(self.driver)

    @property
    def adress_info(self):
        return AdressInfoPage(self.driver)

    @property
    def adress_refion(self):
        return AdressRefionPage(self.driver)