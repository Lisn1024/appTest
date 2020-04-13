"""
功能描述：配置邮件，实现发送邮件的功能

解析：
    1-读取配置，调用readconfig
    2-创建邮件连接配置（host，username……）
    3-创建邮件内容（添加附件report）
    4-调用发送邮件的方法


"""
from common.readConfig1 import ReadConfig
import smtplib,os,time
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
report = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) \
       + "\\" + 'testReport' + "\\" + "test.html"

class configEmail(object):
    #属性
    def __init__(self):
        #读取配置
        conf_list = ReadConfig()
        conf_list = conf_list.get_emailall()
        self.mail_host = conf_list[0][1]
        self.sender = conf_list[4][1]
        self.receiver = conf_list[5][1]
        self.mail_user = conf_list[1][1]
        self.mail_pwd = conf_list[2][1]
        self.subject = conf_list[6][1]
        self.content = conf_list[7][1]

        self.title = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        with open(report,'rb') as file:
            mail_body = file.read()
            #定义邮件内容
            self.msg = MIMEMultipart()
            self.body = MIMEText(self.content, 'plain', 'utf-8')
            self.msg['From'] = self.sender
            self.msg['To'] = self.receiver
            self.msg['Subject'] = Header(self.subject,'utf-8')
            self.msg.attach(self.body)


            att = MIMEText(mail_body, 'html', 'utf-8')
            att['Content-Type'] = 'application/octet-stream'
            att["Content-Disposition"] = 'attachment; filename={}.html'.format(self.title)
            self.msg.attach(att)
        #方法

    def send_mail(self):
        s = smtplib.SMTP()
        s.connect(self.mail_host,25)
        s.login(self.mail_user,self.mail_pwd)
        s.sendmail(self.sender,self.receiver,self.msg.as_string())



if __name__ == '__main__':
    ce = configEmail()
    ce.send_mail()