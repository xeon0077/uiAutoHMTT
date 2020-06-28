"""Page对象工厂"""
from page.page_mp_login import PageMpLogin


class Page:
    # 初始化 driver
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)
