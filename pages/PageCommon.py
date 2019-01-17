#encoding:utf-8


class PageCommon(object):
    def __init__(self,helper):
        self.helper = helper

    def getHomeTab(self):
        return self.helper.findById("net.oschina.app:id/nav_item_news")

    def getMomentTab(self):
        return self.helper.findById("net.oschina.app:id/nav_item_tweet")

    def getPublishBtn(self):
        return self.helper.findById("net.oschina.app:id/nav_item_tweet_pub")

    def getExploreTab(self):
        return self.helper.findById("net.oschina.app:id/nav_item_explore")

    def getMySettingTab(self):
        return self.helper.findById("net.oschina.app:id/nav_item_me")

    def clickHomeTab(self):
        self.helper.click(self.getHomeTab())

    def clickMomentTab(self):
        self.helper.click(self.getMommentTab())

    def clickPublishBtn(self):
        self.helper.click(self.getPublishBtn())

    def clickExploreTab(self):
        self.helper.click(self.getExploreTab())

    def clickMySettingTab(self):
        self.helper.click(self.getMySettingTab())

    def getScreenShot(self,fileName):
        self.helper.get_screenshot(fileName)

    def goBack(self):
        self.helper.goBack()

    def clickEnterKey(self):
        self.helper.clickEnterKey()

    def waitActivity(self,activity):
        self.helper.waitActivity(activity)

    def switchWebView(self):
        self.helper.swithContext("WEBVIEW_net.oschina.app")

    def switchNative(self):
        self.helper.swithContext("NATIVE_APP")

    def getContexts(self):
        return self.helper.getContexts()
