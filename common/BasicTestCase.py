#encoding:utf-8

import  unittest
import  os
import  sys
from appium import  webdriver
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.Helper import  Helper
from common.PageHelper import  PageHelper


class BasicTestCase(unittest.TestCase):

    app_path = os.path.join(r"D:\python\Test_App\osc_test", "app", "osc-android-v4.3.1-release.apk")
    chromedriver_path = os.path.join(r"D:\python\Test_App\osc_test", "app", "chromedriver.exe")
    def setUp(self):
        desired_caps = {}
        desired_caps['app'] = self.app_path
        desired_caps['appPackage'] = "net.oschina.app"
        desired_caps['appActivity'] = ".improve.main.splash.SplashActivity"
        desired_caps['deviceName'] = "CQ3000AUZ6"
        desired_caps['platformVersion'] = '9'
        # desired_caps['deviceName'] = "127.0.0.1:52001"
        # desired_caps['platformVersion'] = '5.1.1'
        desired_caps['platformName'] = 'Android'
        desired_caps['noReset'] = True
        desired_caps['unicodeKeyboard'] = True
        desired_caps['resetKeyboard'] = True
        desired_caps['chromedriverExecutable'] = self.chromedriver_path
        #因为google已经废弃了UIAutomator1，防止有些activity里面的控件获取不到
        #所以使用automationName = “UIAutomator2”
        desired_caps['automationName'] = "UIAutomator2"
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        print(self.driver.get_window_size())
        self.helper = Helper(self.driver)
        self.pagehelper = PageHelper(self.helper)
        self.logoutInit()




    def logoutInit(self):
        try:
            self.pagehelper.getPageCommon().clickMySettingTab()
            if self.pagehelper.getPageMySettings().getNickName().strip() != "点击头像登录":
                self.pagehelper.getPageMySettings().clickSettingsItems()
                self.pagehelper.getPageSettings().clickLogoutBtn()
                self.pagehelper.getPageCommon().goBack()
            self.pagehelper.getPageCommon().clickHomeTab()
        except Exception :
            print("登出异常！")
            self.pagehelper.getPageCommon().getScreenShot("LogoutException")




    def tearDown(self):
        self.driver.quit()



