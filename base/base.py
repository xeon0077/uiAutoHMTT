# 存储web项目和app项目专属方法
import allure
from selenium.webdriver.support.wait import WebDriverWait

from tools.get_log import GetLog

log = GetLog.get_logger()


class Base:
    # 初始化-->解决driver
    def __init__(self, driver):
        log.info("正在初始化driver对象: {}".format(driver))
        self.drvier = driver

    # 查找元素 (输入,点击,获取)
    def base_find(self, loc, timeout=30, poll=0.5):
        '''

        :param loc:By定位方式和对应的值   格式:列表或元祖
        :param timeout:超时时间  默认30秒
        :param poll:访问频率  默认0.5
        :return:元素
        '''
        log.info("正在查找:{}元素,访问频率:{},超时时间:{}".format(loc, poll, timeout))
        # 重点:必须返回
        return WebDriverWait(self.drvier,
                             timeout=timeout,
                             poll_frequency=poll).until(lambda x: x.find_element(*loc))
        # 不能写driver.find_element,会执行
        # 因为底层要的是方法

    # 输入方法封装
    def base_input(self, loc, value):
        '''
        :param loc:参考查找元素
        :param value: 要输入的文本内容
        :return:
        '''
        # 1.获取元素
        log.info("正在准备对:{}元素进行清空操作".format(loc))
        el = self.base_find(loc)  # self.base_find(loc)→调用上面查找元素的方法

        # 2.清空操作
        el.clear()
        log.info("对:{}元素进行清空操作完成".format(loc))
        # 3.输入操作
        log.info("对:{}元素执行输入:{}操作完成".format(loc,value))
        el.send_keys(value)

    # 点击方法封装
    def base_click(self, loc):
        log.info("正在准备对:{}元素进行点击操作".format(loc))
        self.base_find(loc).click()
        log.info("对:{}元素点击操作完成".format(loc))

    # 获取文本方法
    def base_get_text(self, loc):
        """
        :param loc:为列表或元祖
        :return: 元素的文本值
        """
        # 重点:1.必须返回   2.text没有小括号
        log.info("正在准备对:{}元素获取文本操作,获取的文本值:{}".format(loc,self.base_find(loc).text))

        return self.base_find(loc).text

    # 截图
    def base_get_img(self):
        log.error('错误!,正在截图操作')
        # 1.调用截图
        self.drvier.get_screenshot_as_file("./image/err.png")
        #     2.将图片写入报告
        self.__write_img_report()

    # 将图片写入allure报告
    def __write_img_report(self):
        log.error('错误!,正在将图片写入报告操作')

        with open("./image/err.png", "rb")as f:
            allure.attach("描述", f.read(), allure.attach_type.PNG)
