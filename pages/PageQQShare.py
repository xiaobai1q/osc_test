#encoding:utf-8

class PageQQShare():
    def __init__(self,helper):
        self.helper = helper

    def getQQSpaceTextView(self):
        return self.helper.findByText("QQ空间")

    def getCancelBtn(self):
        return self.helper.findById("com.tencent.mobileqq:id/ivTitleBtnRightText")

    def getSearchEditText(self):
        return self.helper.findById("com.tencent.mobileqq:id/et_search_keyword")

    def getTitleTextView(self):
        return self.helper.findById("com.tencent.mobileqq:id/ivTitleName")

    def clickCancelBtn(self):
        self.helper.click(self.getCancelBtn())

    def clickQQSpaceLayout(self):
        self.helper.click(self.getQQSpaceTextView())

    def enterSearchEditText(self,search):
        self.helper.enter(self.getSearchEditText(),search)

    def getTitle(self):
        return self.helper.getText(self.getTitleTextView())





