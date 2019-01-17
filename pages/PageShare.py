#encoding:utf-8
import  random

class PageShare():
    def __init__(self,helper):
        self.helper = helper


    #通过Text内容定位元素
    def getQQShareBtn(self):
        return self.helper.findByText("QQ")

    def getMoreBtn(self):
        return self.helper.findByText("更多")

    def getMomentShareBtn(self):
        return self.helper.findByText("朋友圈")

    #使用坐标定位元素
    def getQQShareBtnByMetric(self):
        start = (810,1632)
        end = (1080,1833)
        return self.helper.getMetricXY(start,end)

    def clickQQShareBtn(self):
        if self.getQQShareBtn():
            self.helper.click(self.getQQShareBtn())
        else:
            print("控件找不到！")
        #self.helper.clickWithMetric(self.getQQShareBtnByMetric())

    def clickMoreBtn(self):
        self.helper.click(self.getMoreBtn())

    def clickMomentShareBtn(self):
        self.helper.click(self.getMomentShareBtn())

    def isSharePage(self):
        return True if self.getMomentShareBtn() else False


