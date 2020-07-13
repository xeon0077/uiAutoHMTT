import pytest

from page.page import Page
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()

class TestMisLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_web_driver(page.mis_url)
        # 获取PageMisLogin对象
        self.login = Page(self.driver).page_get_PageMisLogin()


    # 结束
    def teardown_class(self):
        # 关闭drive
        GetDriver.close_web_driver()

    # 登录测试方法
    @pytest.mark.parametrize('username,password,expect',read_yaml("mis_login.yaml"))
    def test_mis_login(self, username,password,expect):
       try:
            # 调用组合登录业务方法
            self.login.page_mis_login(username,password)
            nickname = self.login.get_nickname()
            print("登录的用户为:", nickname)
            assert expect == nickname, "断言出错,获取的信息为:{},预期结果为:{}".format(nickname, expect)

       except AssertionError as e:
            # 1.日志
            log.error(e)

            # 2.截图
            self.login.base_get_img()
            # 3.抛异常
            raise e
