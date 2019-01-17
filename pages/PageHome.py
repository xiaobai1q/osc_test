#encoding:utf-8

class PageHome(object):
    def __init__(self,helper):
        self.helper = helper

    def getNewsTextView(self,index):
        return self.helper.findById("net.oschina.app:id/tv_title",index=index+5)

    def getNewsTitle(self,index):
        return self.helper.getText(self.getNewsTextView(index=index))

    def clickNewsTextView(self,index):
        self.helper.click(self.getNewsTextView(index=index))
