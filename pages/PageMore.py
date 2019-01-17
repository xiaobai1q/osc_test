#encoding:utf-8
class PageMore():
    def __init__(self,helper):
        self.helper = helper

    def getShareMsgBtn(self):
        return self.helper.findByText("Messages")

    def clickShareMsgBtn(self):
        self.helper.click(self.getShareMsgBtn())

