from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageLocators.login_page_locator import LoginPageLocators as loc
from Common.basepage import BasePage
class LoginPage(BasePage):
    #属性
    # def __init__(self,drvier):
    #     # self.driver = webdriver.Chrome()
    #     self.driver = drvier

    #登录功能
    def login(self,user,password):

        #WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc.use_loc))
        # self.driver.find_element(*loc.use_loc).send_keys(user)
        # self.driver.find_element(*loc.password_loc).send_keys(password)
        # self.driver.find_element(*loc.login_button_loc).click()
        #输入用户名，输入密码，点击登录
        self.input_text(loc.use_loc,"登录面页_输入用户名",user)
        self.input_text(loc.password_loc,"登录面页_输入密码",password)
        self.click_element(loc.login_button_loc,"登录面页_点击登录按钮")

    # 获取表单区域错误信息--账户错误、无密码等
    #//div[@class='form-error-info']
    def get_error_message_loginFrom(self):
         # loc= (By.XPATH,"//div[@class='form-error-info']")
         # WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(loc.error_notify_from_loginFrom))
         # text=self.driver.find_element(*loc.error_notify_from_loginFrom).text
         self.wait_eleVisible(loc.error_notify_from_loginFrom,img_doc="登录面页-等待表单区域错误信息")
         text = self.get_element_text(loc.error_notify_from_loginFrom,img_doc="登录面页-返回表单区域错误信息")
         return text

    #获取面页中间错误信息--没有注册过的账户、密码错误
    #//div[@class='layui-layer-content']
    def get_error_message_pagetCenter(self):
        # loc = (By.XPATH,"//div[@class='layui-layer-content']")
        # WebDriverWait(self.driver,20).until(EC.visibility_of_all_elements_located(loc.error_notify_from_pageCenter))
        # text = self.driver.find_element(*loc.error_notify_from_pageCenter).text
        self.wait_eleVisible(loc.error_notify_from_pageCenter,img_doc="登录面页-等待面页中间错误信息")
        text = self.get_element_text(loc.error_notify_from_pageCenter,img_doc="登录棉业-返回面页中间错误信息")
        return text


