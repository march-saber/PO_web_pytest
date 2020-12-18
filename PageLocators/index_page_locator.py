from selenium.webdriver.common.by import By

class IndexPageLocator:
    #关于我们
    about_us = (By.XPATH,'//a[text()="关于我们"]')
    #用户昵称
    user_name = (By.XPATH,'//a[@href="/Member/index.html"]')
    #首页抢投标按钮
    invest_button = (By.XPATH,'//a[@class="btn btn-special"]')