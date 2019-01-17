#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
from utils.ExcelUtils import ExcelUtils
import  unittest
import os
from ddt import  ddt,unpack,data
import time

@ddt
class LoginCheck(BasicTestCase):
    app_path = os.path.join(PROJECT_PATH, "app", "osc-android-v4.3.1-release.apk")
    test_data_path = os.path.join(PROJECT_PATH, "app", "osc_test_data.xls")
    utils = ExcelUtils(test_data_path, "login_data")
    login_data = utils.get_data()

    @data(*login_data)
    def testLogin(self,login_data):
        u"登陆测试用列"
        self.pagehelper.getPageCommon().clickMySettingTab()
        self.pagehelper.getPageMySettings().clickMyPortraitItems()
        time.sleep(5)
        print(self.driver.current_activity)
        self.pagehelper.getPageLogin().login(login_data['userName'],login_data['passWord'])
        self.assertEqual(self.pagehelper.getPageMySettings().getNickName(), "gexiaoyan1")
        self.pagehelper.getPageCommon().getScreenShot("LoginSuccessful")


if __name__ == '__main__':
    unittest.main()