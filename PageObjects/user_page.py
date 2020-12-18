from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Common.basepage import BasePage
from PageLocators.user_page_locator import UserPageLocator as loc

class UserPage(BasePage):
    # 获取用户余额
    def get_user_leftMoney(self):
        doc = "个人页面_获取账户余额"
        #等待个人信息可见
        #self.wait_eleVisible(loc.user_message_visible,img_doc=doc)
        self.wait_eleVisible(loc.user_leftMoney, img_doc=doc)
        #获取用户余额
        text =self.get_element_text(loc.user_leftMoney,img_doc=doc)
        left_money = text.strip("元") #删除首尾不需要的字符
        return left_money



