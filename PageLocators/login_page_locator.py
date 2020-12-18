#首页元素定位
from selenium.webdriver.common.by import By

class LoginPageLocators:
    #账号输入框
    use_loc = (By.XPATH,"//input[@name='phone']")
    #密码输入框
    password_loc = (By.XPATH,"//input[@name='password']")
    #登录按钮
    login_button_loc = (By.XPATH,'//button[@type="button"]')
    #提示框--登录表单区域
    error_notify_from_loginFrom = (By.XPATH,"//div[@class='form-error-info']")
    #提示框--面页中间区域
    error_notify_from_pageCenter = (By.XPATH,"//div[@class='layui-layer-content']")