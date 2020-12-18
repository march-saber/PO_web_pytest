import unittest
import ddt
import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import login_data as lwd
from TestDatas import Comm_data


@pytest.mark.usefixtures("open_url")  # conftest文件中，fixture下定义的函数名作为返回值
@pytest.mark.usefixtures("refresh_page")
class TestLogin:
    # 异常登录--没有手机号、没有密码、手机号位数不对
    @pytest.mark.login
    @pytest.mark.parametrize("data",lwd.wrong_data)
    def test_login_0_failed_wrong_datas(self, data, open_url):
        # 登录操作
        LoginPage(open_url).login(data['user'], data['passwd'])
        # 断言
        assert LoginPage(open_url).get_error_message_loginFrom(), data['check']

    # 异常场景--错误手机号、密码错误
    @pytest.mark.login
    @pytest.mark.parametrize("data",lwd.fail_data)
    def test_login_1_failed_error_data(self, data, open_url):
        # 登录操作
        LoginPage(open_url).login(data['user'], data['passwd'])
        # 断言
        assert data["check"] == LoginPage(open_url).get_error_message_pagetCenter()

    # 正确登录成功
    @pytest.mark.login
    def test_login_2_success(self, open_url):  # open_url = driver，函数名作为返回值，多个可用a,b,c = open_url,返回abc
        # 步骤+断言
        LoginPage(open_url).login(lwd.success_data['phone'], lwd.success_data['password'])  # 登录
        # 断言
        assert IndexPage(open_url).check_name_exists()  # 断言：判断为True
        # 断言二 --url的变化
        assert open_url.current_url == lwd.success_data['check']
        return open_url
