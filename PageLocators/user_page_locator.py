from selenium.webdriver.common.by import By

class UserPageLocator:
    #可用余额
    user_leftMoney = (By.XPATH,'//li[@class="color_sub"]')
    #个人信息
    user_message_visible = (By.XPATH,'//div[@class="float_left sub_tit_sty" and text()="个人信息"]')