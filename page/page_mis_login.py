import time

import page
from base.base import Base
from tools.get_log import GetLog

log = GetLog.get_logger()

class PageMisLogin(Base):
    # 1.输入用户名
    def page_input_username(self,username):
        self.base_input(page.mis_username,username)
    # 2.输入密码
    def page_input_password(self,password):
        self.base_input(page.mis_password,password)


    # 3.点击登录
    def page_click_login_btn(self):
        # 重点1.执行js语句,修改按钮为可点击
        js = "document.getElementById('inp1').disabled=false"
        self.driver.execute_script(js)
        # 重点2.强制等待2秒钟
        time.sleep(1)

        self.base_click(page.mis_login_btn)

    # 4.获取昵称
    def get_nickname(self):
        return self.base_get_text(page.mis_nickname)

    # # 组合业务方法
    def page_mis_login(self,username,password):
        log.info("正在调用后台管理登录组合业务方法,用户名:{},密码;{}".format(username, password))

        self.page_input_username(username)
        self.page_input_password(password)
        self.page_click_login_btn()
        # 此处没有获取昵称(不需要组合获取昵称)  属于断言,夸页面不组合
