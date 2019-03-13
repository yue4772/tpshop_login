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
        self.page.mine.click_stting()
        # 判断是否登录
        if not self.page.mine.is_login():
            # 登录
            self.page.login_and_sign_up.input_phone("13800138006")
            self.page.login_and_sign_up.input_password("123456")
            self.page.login_and_sign_up.click_login()
            # 根据toast判断是否登录成功
            assert self.page.login_and_sign_up.is_login_seccess("登录成功")
        # 2. 点击收货地址
        self.page.mine.click_address()

        # 3. 点击新建地址
        self.page.adress_list.click_new_adress()

        # 4. 填写个人信息
        # 4.1 填写联系人
        self.page.adress_info.input_name("张三")

        # 4.2 填写手机号
        self.page.adress_info.input_phone("1888888")

        # 4.3 填写详细地址
        self.page.adress_info.input_adress("二号楼 三单元 106")

        # 4.4 填写所在地区
        self.page.adress_info.click_refion()
        # 4.4.1 选择省、市、区、街道
        self.page.adress_refion.click_city()
        # 确定
        self.page.adress_refion.click_commit()

