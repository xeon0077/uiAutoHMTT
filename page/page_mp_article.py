import time
from time import sleep
from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()
class PageMpArticle(Base):
    # 点击 内容管理
    def page_click_content_manage(self):
        # 必须强制等待 1秒
        sleep(1)
        # 点击内容管理
        self.base_click(page.my_content_manage)

    # 点击 发布文章
    def page_click_publish_article(self):
        self.base_click(page.my_publish_article)

    # 输入 文章标题
    def page_input_title(self, title):
        self.base_input(page.my_title, title)

    # 输入 文章内容
    def page_input_content(self, content):
        # 必须 切换 iframe
        frame = self.base_find(page.my_frame)
        self.driver.switch_to.frame(frame)
        # 输入内容
        self.base_input(page.my_content, content)
        # 必须 回到默认目录
        self.driver.switch_to.default_content()

    # 选择 封面 -> 自动
    def page_click_cover(self):

        self.base_click(page.my_cover)

    # 选择频道
    def page_click_channel(self):
        # 点击 请选择
        self.base_click(page.my_click_select)
        # 小坑：由于频道列表是动态从后台获取，所以需要加个暂停时间
        sleep(1)
        # 点击 具体频道
        self.base_click(page.my_channel)

    # 点击发表
    def page_click_submit(self):
        self.base_click(page.my_publish)

    # 获取发表提示信息
    def page_get_result(self):
        return self.base_get_text(page.my_result)

    # 组合业务方法
    def page_publish_article(self, title, content):
        log.info("正在调用文章业务方法,文章title:{},文章内容:{}".format(title,content))
        self.page_click_content_manage()
        self.page_click_publish_article()
        self.page_input_title(title)
        self.page_input_content(content)
        self.page_click_cover()
        self.page_click_channel()
        self.page_click_submit()

