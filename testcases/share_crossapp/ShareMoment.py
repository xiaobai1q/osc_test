#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest
import  time

class ShareMoment(BasicTestCase):
    '分享微信朋友圈测试用列'
    def testShareMoment(self):
        self.pagehelper.getPageHome().clickNewsTextView(2)
        title = self.pagehelper.getPageNewsDetail().getNewsTitle()
        self.pagehelper.getPageNewsDetail().clickShareBtn()
        self.pagehelper.getPageShare().clickMomentShareBtn()
        time.sleep(3)
        print(self.driver.current_activity)
        self.pagehelper.getPageMomentShareEdit().clearFwdReasonEditText()
        self.pagehelper.getPageMomentShareEdit().enterFwdReasonEditText("test")
        self.pagehelper.getPageMomentShareEdit().clickPostBtn()
        self.assertTrue(self.pagehelper.getPageShare().isSharePage())

if __name__ == '__main__':
    unittest.main()
