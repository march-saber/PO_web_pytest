import unittest
import ddt
import logging
import time
import pytest

from selenium import webdriver

from Common import logger
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_data as lwd
from TestDatas import Comm_data as CD
from PageObjects.bid_page import BidPage
from TestDatas import invest_data as Ind
from PageObjects.user_page import UserPage


# 步骤
"""
1、首页 - 选一个标，进入标页面
2、投资页面 - 输入金额，进行投资
"""
# 断言
"""
1、个人页面 - 个人余额少的部分 == 投资前的金额 - 投资后的金额
2、投资记录
3、标的可投金额  - 投资金额 = 投资之后的金额 
"""


# @pytest.mark.invset
# @ddt.ddt
@pytest.mark.usefixtures("open_invest_url")
@pytest.mark.usefixtures("refresh_invest_page")
class TestInvest:
    # 用例三部曲，前置，步骤，断言
    # @classmethod
    # def setUpClass(cls):
    #     logging.info("=====用例类前置：初始化浏览器会话，登陆前程贷系统=======")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.maximize_window()
    #     cls.driver.get(CD.web_login_url)      # 登录网址
    #     LoginPage(cls.driver).login(user=CD.user,password=CD.password)    # 输入密码
    #     #首页 - 选一个标来投资 - 直接选第一个标 - --- / 随机选一个
    #     IndexPage(cls.driver).click_invest_button()
    #     cls.bid_page = BidPage(cls.driver)
    #
    # def tearDown(self):
    #     logging.info("=====每一个用例后置：刷新当前页面=======")
    #     self.driver.refresh()
    #     time.sleep(0.5)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     logging.info("=====用例类后置：关闭浏览器会话,清理环境=======")
    #     cls.driver.quit()

    # @ddt.data(*Ind.wrong_format_money)
    @pytest.mark.smoke1
    @pytest.mark.parametrize("data",Ind.wrong_format_money)
    def test_invest_0_failed_by_No100(self,data,open_invest_url):
        self.driver, self.bid_page = open_invest_url
        logging.info("*********投资用例：异常场景：投资金额为非100的整数倍、错误的格式等*********")
        # 投标页面 - 获取投资前的个人余额
        user_money_beforeInvset = self.bid_page.get_user_money()
        # 投标页面-输入金额，点击投标
        self.bid_page.invset(data["money"])
        # 获取提示信息
        errorMsg = self.bid_page.get_errorMsg_from_pageCenter()
        #刷新
        self.driver.refresh()
        #获取投标页面--个人余额
        user_money_afterInvset = self.bid_page.get_user_money()
        #断言---首先断言错误信息试提示是否正确，然后断言金额没有发生变化
        assert data["check"] == errorMsg
        assert user_money_beforeInvset == user_money_afterInvset

    @pytest.mark.smoke1
    def test_invest_1_success(self,open_invest_url):
        self.driver, self.bid_page = open_invest_url
        logging.info("*********投资用例：正常场景-投资成功*********")
        # 投标页面 - 获取投资前的个人余额
        userMoney_beforeInvset = self.bid_page.get_user_money()
        # 投标页面-输入金额，点击投标
        self.bid_page.invset(Ind.success["money"])
        # 标页面 - 投资成功弹出框 ，点击查看并激活按钮
        self.bid_page.click_activeButton_on_success_popup()
        # 验证
        # 个人页面 - 获取用户投资后当前余额
        userMoney_leftInvset = UserPage(self.driver).get_user_leftMoney()
        # 断言--投资前的余额减去投资后的，应该等于投资的
        assert Ind.success["money"] == int(float(userMoney_beforeInvset) - float(userMoney_leftInvset))

