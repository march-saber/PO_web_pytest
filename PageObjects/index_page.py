from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from  PageLocators.index_page_locator import IndexPageLocator as loc
from Common.basepage import BasePage

class IndexPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    #检查昵称是否存在 存在返回true，不存在返回false
    def check_name_exists(self):
        self.wait_eleVisible(loc.about_us,"首页—等待关于我们元素可见")
        # WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located(loc.about_us))   #等待周围元素可见
        time.sleep(0.5)
        try:
            self.get_element(loc.user_name,"首页-找到用户昵称元素")
            # self.driver.find_element(*loc.user_name)
            return True
        except:
            return False

    #点击投标按钮--第一个抢投标
    def click_invest_button(self):
        self.wait_eleVisible(loc.invest_button,"首页-找到抢投标按钮")
        # WebDriverWait(self.driver,5).until(EC.visibility_of_all_elements_located(loc.invest_button))
        try:
            self.click_element(loc.invest_button,img_doc="首页-点击抢投标按钮")
            return True
            # return self.driver.find_element(*loc.invest_button).click()
        except:
            return False