import datetime
import logging
import time
from Common import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from Common.dir_config import screenshot_dir


class BasePage:
    # 包含了PageObjects当中，用到所有的selenium底层方法。
    # 还可以包含通用的一些元素操作，如alert,iframe,windows...
    # 还可以自己额外封装一些web相关的断言
    # 实现日志记录、实现失败截图
    def __init__(self,driver):
        self.driver = driver

    def wait_eleVisible(self,loc,img_doc ="" ,timeout=30,frequency=0.5):
        logging.info("等待元素{}可见".format(loc))
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver,timeout,frequency).until(EC.visibility_of_element_located(loc))
            end = datetime.datetime.now()
            logging.info("开始时间{}，结束时间{}，等待时长{}".format(start,end,(end-start)))
        except:
            #日志
            logging.exception("等待元素可见失败")
            # 截图 - 哪一个页面哪一个操作导致的失败。+ 当前时间
            self.save_web_screenshot(img_doc)
            raise

    # 查找/发现一个元素
    def get_element(self,loc,img_doc=''):
        logging.info("开始查找{}元素".format(loc))
        try:
            ele = self.driver.find_element(*loc)
            return ele
        except:
            logging.exception("查找{}元素失败".format(loc))
            #截图
            self.save_web_screenshot(img_doc)
            raise

    #等待元素可见，找元素，然后再去点击元素
    def click_element(self,loc,img_doc='',timeout=22,frozenset=0.5):
        self.wait_eleVisible(loc,img_doc,timeout,frozenset)
        ele = self.get_element(loc,img_doc)
        logging.info("开始点击元素{}".format(loc))
        try:
            ele.click()
        except:
            logging.exception("元素{}点击失败".format(loc))
            self.save_web_screenshot(img_doc)
            raise

    # 文本输入
    def input_text(self,loc,img_doc='',*args):
        #等待元素可见
        self.wait_eleVisible(loc,img_doc = img_doc)
        #查找元素
        ele = self.get_element(loc,img_doc = img_doc)
        #在操作
        logging.info("给元素{}输入{}文本值".format(loc,args))
        try:
            ele.send_keys(*args)
        except:
            logging.exception("元素输入操作失败")
            #截图
            self.save_web_screenshot(img_doc)

    # 获取元素的属性值--即为元素的值
    def get_element_attribute(self,loc,attr_name,img_doc):
        #查找到相关元素
        ele = self.get_element(loc,img_doc)
        try:
            attr_value = ele.get_attribute(attr_name)
            logging.info("元素{}的属性{}的值为{}".format(loc,attr_name,attr_value))
            return attr_value
        except:
            logging.exception("获取元素{}属性{}的值失败".format(loc,attr_name))
            self.save_web_screenshot(img_doc)
            raise

    # 获取元素的文本值。
    def get_element_text(self,loc,img_doc):
        # 等待元素
        # self.wait_eleVisible(loc)
        #查找元素
        ele = self.get_element(loc)
        try:
            text = ele.text
            logging.info("获取{}元素的文本值为{}".format(loc,text))
            return text
        except:
            logging.exception("获取{}元素文本值失败".format(loc))
            self.save_web_screenshot(img_doc)
            raise

    # 实现网页截图操作
    def save_web_screenshot(self,img_doc):
        #  页面_功能_时间.png
        now = time.strftime("%Y-%m-%d %H_%M_%S")
        filepath = ("{}_{}.png".format(img_doc,now))  #保存截图的名称
        try:
            self.driver.save_screenshot(screenshot_dir + '/' + filepath)
            logging.info("网页截图成功。图片存储在：{}".format(screenshot_dir +"/" + filepath))
        except:
            logging.exception("网页截屏失败")
