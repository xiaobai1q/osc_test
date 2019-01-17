#encoding:utf-8
import  smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

class MailUtils(object):
    def __init__(self,mailinfo):
        self.mailinfo = mailinfo

    def send_mail(self):
        message = MIMEMultipart()
        message['From'] = self.mailinfo['sender']
        message['To'] = self.mailinfo['receiver']
        message['Subject'] = self.mailinfo['subject']
        message.attach(MIMEText(self.mailinfo['content'],\
                                self.mailinfo['subtype'],\
                                self.mailinfo['charset']))
        attach1 = MIMEText(self.mailinfo['content'],\
                          'base64',self.mailinfo['charset'])
        attach1['Content-Type'] = "application/octet-stream"
        attach1['Content-Disposition'] = "attachment;filename=%s" % self.mailinfo['filename']
        message.attach(attach1)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.mailinfo['mailserver'])
            smtp.login(self.mailinfo['sender'], self.mailinfo['auth_code'])
            smtp.sendmail(from_addr=self.mailinfo['sender'],\
                          to_addrs=self.mailinfo['receiver'].split(','),\
                          msg=message.as_string())
            smtp.quit()
            print("发送成功！")
        except Exception as reason:
            print(reason)
            print("发送失败！")


if __name__ == '__main__':
    with open("2018-11-05 08_27_36_api_result.html","rb") as file:
        content = file.read()
        mailinfo = {
            "sender":"xiaobai1q@163.com",
            "receiver":'xiaobairena1q@163.com,598520439@qq.com',
            "mailserver":"smtp.163.com",
            "subject":"测试",
            "subtype":"html",
            "charset":"utf-8",
            "content": content,
            "auth_code":"gexiaoyan123456",
            "filename":"test_result.html"
        }
        utils = MailUtils(mailinfo)
        utils.send_mail()