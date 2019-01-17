#encoding:utf-8

class PageMomentShareEdit():
    def __init__(self,helper):
        self.helper = helper

    def getFwdReasonEditText(self):
        return self.helper.findById("com.tencent.mm:id/cib")

    def getPostBtn(self):
        return self.helper.findById("com.tencent.mm:id/j0")

    def clearFwdReasonEditText(self):
        self.helper.clear(self.getFwdReasonEditText())

    def enterFwdReasonEditText(self,reason):
        self.helper.enter(self.getFwdReasonEditText(),reason)

    def clickPostBtn(self):
        self.helper.click(self.getPostBtn())


