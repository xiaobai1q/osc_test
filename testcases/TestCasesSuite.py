#encoding:utf-8
import  unittest
import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from  login.LoginCheck import  LoginCheck
from  login.LoginPermissionCheck import LoginPremissionCheck
from versioncheck.VersionCheck import VersionCheck
from myreadcheck.MyReadsCheck import MyReadsCheck
from share_crossapp.ShareMoment import  ShareMoment
from share_crossapp.ShareMsg import  ShareMsg
from share_crossapp.ShareTOQQ import ShareToQQ
from webview.WebView import WebView
from utils.MailUtils import MailUtils
from HTMLTestRunner import  HTMLTestRunner
import  time
import os


def getSuite():
    login_test_cases = unittest.TestLoader().loadTestsFromTestCase(LoginCheck)
    loginPremission_test_cases = unittest.TestLoader().loadTestsFromTestCase(LoginPremissionCheck)
    versionCheck_test_cases = unittest.TestLoader().loadTestsFromTestCase(VersionCheck)
    myreads_test_cases = unittest.TestLoader().loadTestsFromTestCase(MyReadsCheck)
    sharemsg_test_cases = unittest.TestLoader().loadTestsFromTestCase(ShareMsg)
    sharemoment_test_cases = unittest.TestLoader().loadTestsFromTestCase(ShareMoment)
    sharetoQQ_test_cases = unittest.TestLoader().loadTestsFromTestCase(ShareToQQ)
    webview_test_cases = unittest.TestLoader().loadTestsFromTestCase(WebView)
    suite = unittest.TestSuite()
    #suite.addTests([login_test_cases,])
    suite.addTests([loginPremission_test_cases,login_test_cases,\
                    versionCheck_test_cases,myreads_test_cases, \
                    sharemsg_test_cases,sharemoment_test_cases,
                    sharetoQQ_test_cases,webview_test_cases,])
    return suite

def send_report(filePath):
    with open(filePath, "rb") as file:
        content = file.read()
        mailinfo = {
            "sender": "xiaobai1q@163.com",
            "receiver": 'xiaobairena1q@163.com,598520439@qq.com',
            "mailserver": "smtp.163.com",
            "subject": "登陆测试用例执行结果",
            "subtype": "html",
            "charset": "utf-8",
            "content": content,
            "auth_code": "gexiaoyan123456",
            "filename": "osc_app_test_result.html"
        }
        utils = MailUtils(mailinfo)
        utils.send_mail()


if __name__ == '__main__':
    suite = getSuite()
    filePath = PROJECT_PATH+os.sep+"testReport"+os.sep+time.strftime("%Y-%m-%d %H_%M_%S", time.localtime()) + "_osc_app_result.html"
    with open(filePath, "wb") as file:
        runner = HTMLTestRunner(stream=file, verbosity=2, title="开源中国app测试报告", description="登陆测试用例执行结果:")
        runner.run(suite)
    send_report(filePath)


