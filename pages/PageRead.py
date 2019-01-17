#encoding:utf-8

class PageRead(object):
    def __init__(self,helper):
        self.helper = helper

    def getReadsTitleTextView(self,index):
        return self.helper.findById("net.oschina.app:id/tv_title",index=index-1)

    def getReadsTitle(self,index):
        return self.helper.getText(self.getReadsTitleTextView(index))
