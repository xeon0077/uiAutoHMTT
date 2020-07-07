from selenium.webdriver.common.by import By

'''以下为子系统请求url'''
# 自媒体
mp_url = "http://ttmp.research.itcast.cn/#/login"

# 后台管理
'''以下为自媒体元素配置信息'''
# 手机号
mp_phone = By.CSS_SELECTOR, "[placeholder='请输入手机号']"
# 验证码
mp_code = By.CSS_SELECTOR, '[placeholder="验证码"]'
# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"
# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"



#1. 内容管理
my_content_manage = By.XPATH,"//*[text()='内容管理']"
# 2.点击发布文章
my_publish_article = By.XPATH,"//*[contains(text(),'发布文章')]"
# 3.输入文章标题
my_title=By.CSS_SELECTOR,"[placeholder='文章名称']"
# 必须切换frame
my_frame = By.CSS_SELECTOR,"#publishTinymce_ifr"
# 4.输入文章内容
my_content = By.CSS_SELECTOR,"#tinymce"
# 5.点击封面-->自动
my_cover = By.CSS_SELECTOR,"//*[text()='自动']"
# 6.点击请选择
my_click_select = By.CSS_SELECTOR,"[placeholder='请选择']"
# 点击频道
my_channle = By.XPATH,"//*[text()='数据库']"
# 7.点击发表
my_publish = By.XPATH,"//*[text()='发表']"
# 8.获取发表结果
my_result = By.XPATH,"//*[contains(text(),'新增文章成功')]"

