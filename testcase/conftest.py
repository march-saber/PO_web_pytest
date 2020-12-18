import pytest
from selenium import webdriver
from TestDatas import Comm_data as CD
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage

# driver = None


@pytest.fixture(scope="class") #等于的是作用域
def open_url():
    # 前置
    # global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    yield driver  #可以有多个返回值，逗号隔开，或者元祖形式都行，多个返回的是元祖
    # 后置
    driver.quit()


@pytest.fixture
def refresh_page(open_url):
    yield
    open_url.refresh()


@pytest.fixture(scope="class") #等于的是作用域
def open_invest_url():
    # 前置
    # global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(CD.web_login_url)
    LoginPage(driver).login(user=CD.user,password=CD.password)
    IndexPage(driver).click_invest_button()
    bid_page = BidPage(driver)
    yield driver, bid_page        #可以有多个返回值，逗号隔开，或者元祖形式都行，多个返回的是元祖
    # 后置
    driver.quit()


@pytest.fixture
def refresh_invest_page(open_invest_url):
    yield
    driver, bid_page = open_invest_url
    driver.refresh()

@pytest.fixture(scope="class")
def web_login():
    pass

# def pytest_configure(config):
#     config.addinivalue_line("markers","smoke1:标签只运行冒烟用例")
#     config.addinivalue_line("markers","smoke2:示例运行")