from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from Common.basepage import BasePage
from PageLocators.bid_page_locator import BidPageLocator as loc

class BidPage(BasePage):
    # def __init__(self,driver):
    #     self.driver = driver

    #投资
    def invset(self,money):
        self.input_text(loc.money_input,"投标面页_输入金额",money)
        self.click_element(loc.invest_button,"标面页_投标按钮")

    # 投资成功的提示框 - 点击查看并激活
    def click_activeButton_on_success_popup(self):
        self.click_element(loc.active_button_on_successPop,"投标页面_投资成功的提示框 - 点击查看并激活")

    #获取用户可投余额
    def get_user_money(self):
        self.wait_eleVisible(loc.money_input,"投标页面_等待获取用户余额")
        usemoney = self.get_element_attribute(loc.money_input,"data-amount","投标页面_可投余额")
        return usemoney

    # 错误提示框 - 页面中间-获取错误信息
    def get_errorMsg_from_pageCenter(self):
        self.wait_eleVisible(loc.invest_failed_popup,"投标页面_等待投资失败框")
        meg = self.get_element_text(loc.invest_failed_popup,"投标页面_投资失败提示框_获取错误信息")
        self.click_element(loc.invest_close_failed_popup_button,"投标页面_关闭投资失败提示框")
        return meg






