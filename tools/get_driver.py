from selenium import webdriver


class GetDriver:
    # 定义driver变量
    __web_driver = None

    # 获取web driver
    @classmethod
    def get_web_driver(cls,url):
        if cls.__web_driver == None:
            # 获取浏览器对象
            cls.__web_driver = webdriver.Chrome()
            # 最大化
            cls.__web_driver.maximize_window()
            # 打开url
            cls.__web_driver.get(url)
        # 返回web driver
        return cls.__web_driver
    # 关闭web driver
    @classmethod
    def close_web_driver(cls):
        if cls.__web_driver is not None:
            cls.__web_driver.quit()
            # 置空操作
            cls.__web_driver =None




    # 获取app driver
    def app_driver(self):
        pass

    # 关闭app driver
    def close_app_driver(self):
        pass
