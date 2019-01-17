#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest
import time


class ShareToQQ(BasicTestCase):
    def testShareMag(self):
        u"QQ控件分享测试用例"
        self.pagehelper.getPageHome().clickNewsTextView(2)
        title = self.pagehelper.getPageNewsDetail().getNewsTitle()
        self.pagehelper.getPageNewsDetail().clickShareBtn()
        self.pagehelper.getPageShare().clickQQShareBtn()
        self.pagehelper.getPageQQShare().clickQQSpaceLayout()
        self.pagehelper.getPageQQShareEdit().enterFwdReasonEditText("test")
        self.pagehelper.getPageQQShareEdit().clickPublishBtn()
        self.assertTrue(self.pagehelper.getPageShare().isSharePage())


if __name__ == '__main__':
    unittest.main()
