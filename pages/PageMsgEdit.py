#encoding:utf-8
class PageMsgEdit():
    def __init__(self,helper):
        self.helper = helper

    def getRecipientEditText(self):
        return self.helper.findById("com.google.android.apps.messaging:id/recipient_text_view")

    def getMsgSendBtn(self):
        return self.helper.findById("com.google.android.apps.messaging:id/send_message_button_icon")

    def getNewestMsgContentTextView(self):
        return self.helper.findById("com.google.android.apps.messaging:id/message_text",index=-1)

    def clearRecipientEditText(self):
        self.helper.clear(self.getRecipientEditText())

    def enterRecipientEditText(self,recipient):
        self.helper.enter(self.getRecipientEditText(),recipient)

    def clickMsgSendBtn(self):
        self.helper.click(self.getMsgSendBtn())

    def getNewestMsgContent(self):
        return self.helper.getText(self.getNewestMsgContentTextView())


