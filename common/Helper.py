#encoding:utf-8
from selenium.webdriver.common.by import By
from  selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
import os
import  time
import  random

#常用的控件操作

class Helper(object):
    Default_TimeOut = 10
    KEYCODE_ENTER = 66
    KEYCODE_BACK = 4
    BaseWindowSize = {'width': 1080, 'height': 2034}

    def __init__(self,driver):
        self.driver = driver

    #通过指定方式等待元素出现
    def waitForElement(self,by):
        WebDriverWait(self.driver,self.Default_TimeOut).until(
            EC.presence_of_element_located(by)
        )

    #根据元素id定位到该元素,timeOut=0或者不赋值给timeout则不需要延迟
    def findById(self,id,index=0):
        self.waitForElement((By.ID,id))
        return self.driver.find_elements_by_id(id)[index]

    #根据元素类名定位元素,ele为空表示在根节点开始查找,timeOut=0或者不赋值给timeout则不需要延迟
    def findByClassName(self,className,index=0):
        self.waitForElement((By.CLASS_NAME, className))
        return self.driver.find_elements_by_class_name(className)[index]

    #根据元素内容定位元素,timeOut=0或者不赋值给timeout则不需要延迟
    def findByText(self,text,index=0):
        xpath = "//*[@text='{}']".format(text)
        self.waitForElement((By.XPATH,xpath))
        return self.driver.find_elements_by_xpath(xpath)[index]

    #根据元素内容是否包含内容定位元素,timeOut=0或者不赋值给timeout则不需要延迟
    def findByTextContain(self,text,index=0):
        xpath = "//*[contains(@text,'{}')]".format(text)
        self.waitForElement((By.XPATH, xpath))
        return self.driver.find_elements_by_xpath(xpath)[index]

    def click(self,ele):
        print("执行控件点击操作------>")
        ele.click()

    def enter(self,ele,text):
        print("执行输入框输入操作,输入的文本为:",text,"------>")
        ele.send_keys(text)

    def clear(self,ele):
        print("执行输入框清空操作------>")
        ele.clear()

    def enterWithPreClear(self,ele,text):
        print("执行输入之前先清空输入框")
        self.clear(ele)
        self.enter(ele,text)

    def getText(self,ele):
        text = ele.text
        print("获取控件的文本为:{} ------>".format(text))
        return text

    def goBack(self):
        print("按下back键------>")
        self.driver.press_keycode(self.KEYCODE_BACK)

    #截取手机截图
    def get_screenshot(self, filename):
        print("执行截屏操作------>")
        screenshot_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "screenshot",time.strftime("%Y_%m_%d",time.localtime()))
        screenshotName = time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())
        if not os.path.exists(screenshot_path):
            os.makedirs(screenshot_path)
        self.driver.get_screenshot_as_file(
            screenshot_path + os.sep + "%s_screenshot.png" % (screenshotName + "_" + filename))
        print("截屏成功！")

    #等待某个activity出现
    def waitActivity(self,activity):
        print("等待'{}'activity出现".format(activity))
        self.driver.wait_activity(activity,self.Default_TimeOut)

    def clickEnterKey(self):
        print("按下Enter键")
        self.driver.press_keycode(self.KEYCODE_ENTER)

    def getWindowSize(self):
        print("获取当前手机屏幕大小...")
        return self.driver.get_window_size()

    #根据具体手机的分辨率来重新计算元素的坐标
    def getMetricXY(self,start,end):
        windowSize = self.getWindowSize()
        currentWidth = windowSize['width']
        currentHeight = windowSize['height']
        xNewStart = (start[0]*currentWidth)/self.BaseWindowSize['width']
        xNewEnd = (end[0]*currentWidth)/self.BaseWindowSize['width']
        yNewStart =  (start[1]*currentHeight)/self.BaseWindowSize['height']
        yNewEnd = (end[1]*currentHeight)/self.BaseWindowSize['height']
        xMetric = random.randint(int(xNewStart),int(xNewEnd))
        yMetric = random.randint(int(yNewStart),int(yNewEnd))
        return [(xMetric,yMetric)]

    def clickWithMetric(self,positions):
        print(positions)
        self.driver.tap(positions)

    def findByXpath(self,xpath):
        self.waitForElement((By.XPATH,xpath))
        return self.driver.find_element_by_xpath(xpath)

    def getContexts(self):
        return self.driver.contexts

    def swithContext(self,context):
        print("切换context:",context,"------>")
        self.driver._switch_to.context(context)

    def getCurrentContext(self):
        context = self.driver.current_context
        print("获取当前context:",context,"------>")












