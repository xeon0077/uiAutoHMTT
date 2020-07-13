import pytest

from page.page import Page
from tools.get_driver import GetDriver
import page
from tools.get_log import GetLog
from tools.read_yaml import read_yaml
log = GetLog.get_logger()

class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver = GetDriver.get_web_driver(page.mp_url)
        # 获取Page对象
        self.page_in = Page(self.driver)
        # 调用登录成功业务方法
        self.page_in.page_get_PageMpLogin().page_mp_login_success()
        # 获取PageMpArticle对象
        self.article = self.page_in.page_get_PageMpArticle()

    # 结束
    def teardown_class(self):
        # 关闭drive
        GetDriver.close_web_driver()

    # 发布文章测试方法
    @pytest.mark.parametrize('title,content,expect',read_yaml("mp_article.yaml"))
    def test_publish_article(self, title, content,expect):
        try:
            # 调用发布文章业务方法
            self.article.page_publish_article(title, content)
            # 断言 -> 查看发布结果 注意：此处有个小坑，原因：提示消息有时间限制，类似toast消息
            result = self.article.page_get_result()
            print("发布文章的结果为:", result)
            assert expect == result, "断言出错,登录的账号为:{},预期结果为:{}".format(result, expect)
        except Exception as e:
            # 日志
            log.error(e)
            # 截图
            self.article.base_get_img()
            # 抛异常
            raise
