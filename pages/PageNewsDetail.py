#encoding:utf-8

class PageNewsDetail(object):
    def __init__(self,helper):
        self.helper = helper

    def getAddToFavoritesBtn(self):
        return self.helper.findById("net.oschina.app:id/ib_fav")

    def getNewsTitleTextView(self):
        return self.helper.findById("net.oschina.app:id/tv_title")

    def getShareBtn(self):
        return self.helper.findById("net.oschina.app:id/menu_share")

    def getFirstParagraph(self):
        return self.helper.findByXpath("/html/body/div/p[1]")

    def clickAddToFavoritesBtn(self):
        self.helper.click(self.getAddToFavoritesBtn())

    def getNewsTitle(self):
        return self.helper.getText(self.getNewsTitleTextView())

    def clickShareBtn(self):
        self.helper.click(self.getShareBtn())

    def getFirstParagraphText(self):
        return self.helper.getText(self.getFirstParagraph())






