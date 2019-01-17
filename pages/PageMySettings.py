#encoding:utf-8


class PageMySettings(object):
    def __init__(self,helper):
        self.helper = helper

    def getMyPortraitItems(self):
        return self.helper.findById("net.oschina.app:id/iv_portrait")

    def getSettingsItems(self):
        return self.helper.findById("net.oschina.app:id/iv_logo_setting")

    def getLogoZxingItems(self):
        return self.helper.findById("net.oschina.app:id/iv_logo_zxing")

    def getCoverViewItems(self):
        return self.helper.findById("net.oschina.app:id/coverView")

    def getMyMessageItems(self):
        return self.helper.findById("net.oschina.app:id/rl_message")

    def getMyReadItems(self):
        return self.helper.findById("net.oschina.app:id/rl_read")

    def getMyBlogItems(self):
        return self.helper.findById("net.oschina.app:id/rl_blog")

    def getMyQuestionItems(self):
        return self.helper.findById("net.oschina.app:id/rl_info_question")

    def getMyArticleItems(self):
        return self.helper.findById("net.oschina.app:id/rl_info_article")

    def getMyActivitiesItems(self):
        return self.helper.findById("net.oschina.app:id/rl_info_activities")

    def getMyTagsItems(self):
        return self.helper.findById("net.oschina.app:id/rl_info_tags")

    def getMyTeamItems(self):
        return self.helper.findById("net.oschina.app:id/rl_team")

    def getShareItems(self):
        return self.helper.findById("net.oschina.app:id/rl_share")

    def getNick(self):
        return self.helper.findById("net.oschina.app:id/tv_nick")

    def getFavoritesBtn(self):
        return self.helper.findById("net.oschina.app:id/ly_favorite")

    def clickMyPortraitItems(self):
        self.helper.click(self.getMyPortraitItems())

    def clickSettingsItems(self):
        self.helper.click(self.getSettingsItems())

    def clickLogoZxingItems(self):
        self.helper.click(self.getLogoZxingItems())

    def clickCoverViewItems(self):
        self.helper.click(self.getCoverViewItems())

    def clickMyMessageItems(self):
        self.helper.click(self.getMyMessageItems())

    def clickMyReadItems(self):
        self.helper.click(self.getMyReadItems())

    def clickMyBlogItems(self):
        self.helper.click(self.getMyBlogItems())

    def clickMyQuestionItems(self):
        self.helper.click(self.getMyQuestionItems())

    def clickMyArticleItems(self):
        self.helper.click(self.getMyArticleItems())

    def clickMyActivitiesItems(self):
        self.helper.click(self.getMyActivitiesItems())

    def clickMyTagsItems(self):
        self.helper.click(self.getMyTagsItems())

    def clickMyTeamItems(self):
        self.helper.click(self.getMyTeamItems())

    def clickShareItems(self):
        self.helper.click(self.getShareItems())

    def getNickName(self):
        return self.helper.getText(self.getNick())

    def clickFavoritesBtn(self):
        self.helper.click(self.getFavoritesBtn())