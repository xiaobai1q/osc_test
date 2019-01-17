#encoding:utf-8

import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest
import time




class LoginPremissionCheck(BasicTestCase):
    DEFAULTTIMEOUT = 1

    def test_LoginPremission(self):
        u"查看'我的'相关信息必须先登陆测试用例"
        self.pagehelper.getPageCommon().clickMySettingTab()
        self.pagehelper.getPageMySettings().clickMyMessageItems()
        self.check("MyMessage")

        self.pagehelper.getPageMySettings().clickMyReadItems()
        self.check("MyRead")

        self.pagehelper.getPageMySettings().clickMyBlogItems()
        self.check("MyBlog")

        self.pagehelper.getPageMySettings().clickMyQuestionItems()
        self.check("MyQuestion")

        self.pagehelper.getPageMySettings().clickMyArticleItems()
        self.check("MyArticle")

        self.pagehelper.getPageMySettings().clickMyActivitiesItems()
        self.check("MyActivities")

        self.pagehelper.getPageMySettings().clickMyTagsItems()
        self.check("MyTags")

        self.pagehelper.getPageMySettings().clickMyTeamItems()
        self.check("MyTeam")

        self.pagehelper.getPageMySettings().clickShareItems()
        self.check("Share")


    def check(self,fileName):
        self.assertTrue(self.pagehelper.getPageLogin().isLoginPage)
        time.sleep(self.DEFAULTTIMEOUT)
        self.pagehelper.getPageCommon().getScreenShot(fileName)
        self.pagehelper.getPageCommon().goBack()




if __name__ == '__main__':
    unittest.main()




