from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_data as lwd
from TestDatas import Comm_data
import unittest
import ddt

@ ddt.ddt
class TestLogin(unittest.TestCase):
    #用例三步骤：前置，步骤，断言
    @classmethod
    #classmethod方法，主要是为了节省时间，把所有用例都在一个driver里面执行，不重复打开关闭了
    def setUpClass(cls):
        #前置：打开网页，启动浏览器
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get('{}Index/login.html'.format(Comm_data.base_url))

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def tearDown(self):
        self.driver.refresh()

    #正确登录成功
    def test_login_2_success(self):
        #步骤+断言
        LoginPage(self.driver).login(lwd.success_data['phone'],lwd.success_data['password']) #登录
        #断言
        self.assertTrue(IndexPage(self.driver).check_name_exists()) #断言：判断为True
        #断言二 --url的变化
        self.assertEqual(self.driver.current_url,lwd.success_data['check'])

    #异常登录--没有手机号、没有密码、手机号位数不对
    @ddt.data(*lwd.wrong_data)
    def test_login_0_failed_wrong_datas(self,data):
        #登录操作
        LoginPage(self.driver).login(data['phone'],data['password'])
        #断言
        self.assertEqual(LoginPage(self.driver).get_error_message_loginFrom(),data['check'])

    #异常场景--错误手机号、密码错误
    @ddt.data(*lwd.fail_data)
    def test_login_1_failed_error_data(self,data):
        #登录操作
        LoginPage(self.driver).login(data['phone'],data['password'])
        #断言
        self.assertEqual(LoginPage(self.driver).get_error_message_pagetCenter(),data['check'])


