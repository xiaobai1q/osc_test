#encoding:utf-8

import sys
PROJECT_PATH = r"D:\python\Test_App\osc_test"
sys.path.append(PROJECT_PATH)
from common.Helper import Helper
from pages.PageCommon import  PageCommon
from pages.PageLogin import  PageLogin
from pages.PageMySettings import  PageMySettings
from pages.PageSettings import  PageSettings
from pages.PageAbout import  PageAbout
from pages.PageHome import  PageHome
from pages.PageNewsDetail import  PageNewsDetail
from pages.PageRead import  PageRead
from pages.PageShare import  PageShare
from pages.PageQQShare import  PageQQShare
from pages.PageQQShareEdit import  PageQQShareEdit
from pages.PageMore import  PageMore
from pages.PageSelectConversation import  PageSelectConversation
from pages.PageMsgEdit import  PageMsgEdit
from pages.PageMomentShareEdit import  PageMomentShareEdit

class PageHelper(object):
    def __init__(self,helper):
        self.helper = helper
        self.pageCommon = None
        self.pageLogin = None
        self.pageMySettings = None
        self.pageSettings = None
        self.pageAbout = None
        self.pageHome = None
        self.pageNewsDetail = None
        self.pageRead = None
        self.pageShare = None
        self.pageQQShare = None
        self.pageQQShareEdit = None
        self.pageMore = None
        self.pageSelectConversation = None
        self.pageMsgEdit = None
        self.pageMomentShareEdit = None

    def getPageCommon(self):
        if not self.pageCommon:
            self.pageCommon = PageCommon(self.helper)
        return self.pageCommon

    def getPageLogin(self):
        if not self.pageLogin:
            self.pageLogin = PageLogin(self.helper)
        return self.pageLogin

    def getPageMySettings(self):
        if not self.pageMySettings:
            self.pageMySettings = PageMySettings(self.helper)
        return self.pageMySettings

    def getPageSettings(self):
        if not self.pageSettings:
            self.pageSettings = PageSettings(self.helper)
        return self.pageSettings

    def getPageAbout(self):
        if not self.pageAbout:
            self.pageAbout = PageAbout(self.helper)
        return self.pageAbout

    def getPageHome(self):
        if not self.pageHome:
            self.pageHome = PageHome(self.helper)
        return self.pageHome

    def getPageNewsDetail(self):
        if not self.pageNewsDetail:
            self.pageNewsDetail = PageNewsDetail(self.helper)
        return self.pageNewsDetail

    def getPageRead(self):
        if not self.pageRead:
            self.pageRead = PageRead(self.helper)
        return self.pageRead

    def getPageShare(self):
        if not self.pageShare:
            self.pageShare = PageShare(self.helper)
        return self.pageShare

    def getPageQQShare(self):
        if not self.pageQQShare:
            self.pageQQShare = PageQQShare(self.helper)
        return self.pageQQShare

    def getPageQQShareEdit(self):
        if not self.pageQQShareEdit:
            self.pageQQShareEdit = PageQQShareEdit(self.helper)
        return self.pageQQShareEdit

    def getPageMore(self):
        if not self.pageMore:
            self.pageMore = PageMore(self.helper)
        return self.pageMore

    def getSelectConversation(self):
        if not self.pageSelectConversation:
            self.pageSelectConversation = PageSelectConversation(self.helper)
        return self.pageSelectConversation

    def getPageMsgEdit(self):
        if not self.pageMsgEdit:
            self.pageMsgEdit = PageMsgEdit(self.helper)
        return self.pageMsgEdit

    def getPageMomentShareEdit(self):
        if not self.pageMomentShareEdit:
            self.pageMomentShareEdit = PageMomentShareEdit(self.helper)
        return self.pageMomentShareEdit

