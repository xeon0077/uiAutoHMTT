from selenium.webdriver.common.by import By

'''以下为子系统请求url'''
# 自媒体
mp_url = "http://ttmp.research.itcast.cn/#/login"

# 后台管理


'''以下为自媒体登录元素配置信息'''
# 手机号
mp_phone = By.CSS_SELECTOR, "[placeholder='请输入手机号']"

# 验证码
mp_code = By.CSS_SELECTOR, '[placeholder="验证码"]'

# 登录按钮
mp_login_btn = By.CSS_SELECTOR, ".el-button--primary"

# 昵称
mp_nickname = By.CSS_SELECTOR, ".user-name"
