#encoding:utf-8

import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest
import  time


class WebView(BasicTestCase):
    def testWebView(self):
        u"测试切换WebView"
        self.pagehelper.getPageHome().clickNewsTextView(5)
        time.sleep(5)
        print(self.pagehelper.getPageCommon().getContexts())
        self.pagehelper.getPageCommon().switchWebView()
        print(self.pagehelper.getPageNewsDetail().getFirstParagraphText())


if __name__ == '__main__':
    unittest.main()
