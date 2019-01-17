#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest
import  time

class ShareMsg(BasicTestCase):
    DEFAULTTIMEOUT = 2
    def testShare(self):
        u"短信分享测试用例"
        self.pagehelper.getPageHome().clickNewsTextView(2)
        title = self.pagehelper.getPageNewsDetail().getNewsTitle()
        self.pagehelper.getPageNewsDetail().clickShareBtn()
        self.pagehelper.getPageShare().clickMoreBtn()
        self.pagehelper.getPageMore().clickShareMsgBtn()
        self.pagehelper.getSelectConversation().clickNewMsgBtn()
        self.pagehelper.getPageMsgEdit().clearRecipientEditText()
        self.pagehelper.getPageMsgEdit().enterRecipientEditText("15151849942")
        self.pagehelper.getPageCommon().clickEnterKey()
        self.pagehelper.getPageMsgEdit().clickMsgSendBtn()
        time.sleep(self.DEFAULTTIMEOUT)
        self.assertTrue(title in self.pagehelper.getPageMsgEdit().getNewestMsgContent())



if __name__ == '__main__':
    unittest.main()

