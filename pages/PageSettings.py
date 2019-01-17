#encoding:utf-8


class PageSettings(object):
    def __init__(self,helper):
        self.helper = helper

    def getLogoutBtn(self):
        return self.helper.findById("net.oschina.app:id/rl_cancel")

    def getAboutItems(self):
        return self.helper.findById("net.oschina.app:id/rl_about")

    def clickLogoutBtn(self):
        self.helper.click(self.getLogoutBtn())

    def clickAboutItmes(self):
        self.helper.click(self.getAboutItems())