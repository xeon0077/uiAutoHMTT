import page
from page.page import Page
from tools.get_driver import GetDriver

class TestMpArticle:
    # 初始化
    def setup_class(self):
        # 获取driver
        self.driver =GetDriver.get_web_driver(page.mp_url)
        # 获取page对象
        self.page_in = Page(self.driver)
        # 调用登录业务方法对象
        self.page_in.page_get_PageMpLogin(). page_mp_login_success()
        # 获取PageMpArticle对象
        self.article=self.page_in.page_get_PageMpArticle()
    # 结束
    def teardown_class(self):
        # 关闭driver
        GetDriver.close_web_driver()

    # 发布文章测试方法
    def test_publish_article(self, title="bj18-test001", content="今天天气不错,晚上吃点好的"):
            # 调用发布文章业务方法
        self.article.page_publish_article(title,content)
            # 断言-->查看发布结果
        result = self.article.page_get_result()
        print("发布文章的结果为:",result)
