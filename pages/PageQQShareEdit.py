#encoding:utf-8

class PageQQShareEdit():
    def __init__(self,helper):
        self.helper = helper

    def getFwdReasonEditText(self):
        return self.helper.findByText("转发理由...")

    def getPublishBtn(self):
        return self.helper.findById("com.tencent.mobileqq:id/ivTitleBtnRightText")

    def getCancelBtn(self):
        return self.helper.findById("com.tencent.mobileqq:id/ivTitleBtnLeftButton")

    def enterFwdReasonEditText(self,text):
        self.helper.enter(self.getFwdReasonEditText(),text)

    def clickPublishBtn(self):
        self.helper.click(self.getPublishBtn())

    def clickCancelBtn(self):
        self.helper.click(self.getCancelBtn())

