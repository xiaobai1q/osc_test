#encoding:utf-8

class PageSelectConversation():
    def __init__(self,helper):
        self.helper = helper

    def getNewMsgBtn(self):
        return self.helper.findById("android:id/button1")

    def clickNewMsgBtn(self):
        self.helper.click(self.getNewMsgBtn())