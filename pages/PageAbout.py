#encoding:utf-8

class PageAbout(object):
    def __init__(self,helper):
        self.helper = helper

    def getVersionTextView(self):
        return self.helper.findById("net.oschina.app:id/tv_version_name")

    def getVersion(self):
        return self.helper.getText(self.getVersionTextView())
