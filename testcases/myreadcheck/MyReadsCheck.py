#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
from utils.ExcelUtils import ExcelUtils
import  unittest


class MyReadsCheck(BasicTestCase):
    DEFAULTTIMEOUT = 2


    def testAddToFavorites(self):
        u"阅读记录测试用例"
        self.pagehelper.getPageCommon().clickMySettingTab()
        self.pagehelper.getPageMySettings().clickMyPortraitItems()
        self.pagehelper.getPageLogin().login("15151849942","gexiaoyan1q")
        self.pagehelper.getPageCommon().clickHomeTab()
        self.pagehelper.getPageHome().clickNewsTextView(1)
        title = self.pagehelper.getPageNewsDetail().getNewsTitle()
        self.pagehelper.getPageCommon().goBack()
        self.pagehelper.getPageCommon().clickMySettingTab()
        self.pagehelper.getPageMySettings().clickMyReadItems()
        self.assertEqual(self.pagehelper.getPageRead().getReadsTitle(1),title)


if __name__ == '__main__':
    unittest.main()



