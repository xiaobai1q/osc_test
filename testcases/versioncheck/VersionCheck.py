#encoding:utf-8
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.BasicTestCase import  BasicTestCase
import  unittest


class VersionCheck(BasicTestCase):
    def testVersionCheck(self):
        u"检查版本测试用列"
        self.pagehelper.getPageCommon().clickMySettingTab()
        self.pagehelper.getPageMySettings().clickSettingsItems()
        self.pagehelper.getPageSettings().clickAboutItmes()
        self.assertEqual(self.pagehelper.getPageAbout().getVersion(),"v4.2.1 (1810230800)")



if __name__ == '__main__':
    unittest.main()