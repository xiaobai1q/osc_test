#encoding:utf-8

class PageLogin(object):
    def __init__(self,helper):
        self.helper = helper

    def getUserNameEditText(self):
        return self.helper.findById("net.oschina.app:id/et_login_username")

    def getPasswordEditText(self):
        return self.helper.findById("net.oschina.app:id/et_login_pwd")

    def getLoginSubmitBtn(self):
        return self.helper.findById("net.oschina.app:id/bt_login_submit")

    def clickLoginSubmitBtn(self):
        self.helper.click(self.getLoginSubmitBtn())

    def clearUserNameEditText(self):
        self.helper.clear(self.getUserNameEditText())

    def clearPasswordEditText(self):
        self.helper.clear(self.getPasswordEditText())

    def enterUserNameEditText(self,userName):
        self.helper.enter(self.getUserNameEditText(),userName)

    def enterPasswordEditText(self,passWord):
        self.helper.enter(self.getPasswordEditText(),passWord)

    def login(self,userName,passWord):
        self.clearUserNameEditText()
        self.enterUserNameEditText(userName)
        self.clearPasswordEditText()
        self.enterPasswordEditText(passWord)
        self.clickLoginSubmitBtn()

    def isLoginPage(self):
        print("="*30)
        return True if self.getLoginSubmitBtn() else False




