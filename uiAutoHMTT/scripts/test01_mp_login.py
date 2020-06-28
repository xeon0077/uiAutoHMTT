import pytest

from page.page import Page
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml

log = GetLog.get_logger()


class TestMpLogin:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_web_driver(page.mp_url)
        # 获取Page对象
        self.login = Page(self.driver).page_get_PageMpLogin()

    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.close_web_driver()

    # 登录测试方法
    @pytest.mark.parametrize("phone,code,expect", read_yaml("mp_login.yaml"))
    def test_login(self, phone, code, expect):
        try:
            # 调用登录业务方法
            self.login.page_mp_login(phone, code)
            # 断言
            nickname = self.login.page_get_nickname()
            print("获取的昵称为：", nickname)
            assert expect == nickname, "断言出错，登录的账号为：{}, 预期结果为：{}".format(nickname, expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.login.base_get_img()
            # 抛异常
            raise
