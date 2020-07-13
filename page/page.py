from page.page_mis_login import PageMisLogin
from page.page_mp_article import PageMpArticle
from page.page_mp_login import PageMpLogin


class Page:
    # 初始化driver
    def __init__(self, driver):
        self.driver = driver

    # 获取PageMpLogin对象
    def page_get_PageMpLogin(self):
        return PageMpLogin(self.driver)
    # 获取PageMpArticle对象
    def page_get_PageMpArticle(self):
        return PageMpArticle(self.driver)

    # 获取PageMisLogin对象
    def page_get_PageMisLogin(self):
        return PageMisLogin(self.driver)