from base.base import Base
import page
from tools.get_log import GetLog

log = GetLog.get_logger()


class PageMpLogin(Base):
    # 输入手机号
    def page_input_phone(self, phone):
        self.base_input(page.mp_phone, phone)

    # 输入验证码
    def page_input_code(self, code):
        self.base_input(page.mp_code, code)

    # 点击登录
    def page_click_login_btn(self):
        self.base_click(page.mp_login_btn)

    # 获取昵称
    def page_get_nickname(self):
        return self.base_get_text(page.mp_nickname)

    # 组合业务（测试业务层调用）
    def page_mp_login(self, phone, code):
        log.info("正在调用登录组合业务方法，手机号：{} 验证码：{}".format(phone, code))
        self.page_input_phone(phone)
        self.page_input_code(code)
        self.page_click_login_btn()