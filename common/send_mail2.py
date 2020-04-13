import smtplib,os,time
from common.readConfig1 import ReadConfig
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.text import MIMEText
report = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+'\\'+'testReport'+'\\'+'test.html'
class configEmail(object):

    def __init__(self):
        conf_list = ReadConfig()
        conf_list = conf_list.get_emailall()
        self.mail_host = conf_list[0][1]
        self.sender = conf_list[4][1]
        #self.receiver = conf_list[5][1] #单人邮箱格式
        self.mail_user = conf_list[1][1]
        self.mail_pwd = conf_list[2][1]
        self.subject = conf_list[6][1]
        self.content = conf_list[7][1]

        #发多人邮箱格式
        self.receiver = ['lishengnantest@163.com','1473147172@qq.com','1520456621@qq.com','18332300241@163.com']

        #设置附件的动态时间标题名称
        self.title = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        with open(report,encoding='UTF-8') as file:
            mail_body = file.read()
            # 组装邮件内容和标题，中文需参数‘utf-8’
            self.body = MIMEText(self.content, 'plain', 'utf-8')  # 该处为添加邮件正文
            self.msg = MIMEMultipart()
            self.msg['Subject'] = Header(self.subject, 'utf-8')    # 该处为添加邮件标题
            self.msg['From'] = self.sender
            #self.msg['To'] = self.receiver  # 收件人为单人
            self.msg['To'] = ','.join(self.receiver)#与前面发送多人结合使用
            self.msg.attach(self.body)  # 添加正文内容

            #添加附件
            att = MIMEText(mail_body, "plain", "utf-8")
            att["Content-Type"] = "application/octet-stream"
            # att["Content-Disposition"] = 'attachment; filename={}.html'.format(file)#添加文件、及文件名后缀名
            att["Content-Disposition"] = 'attachment; filename={}'.format(self.title)  # 直接添加文件
            self.msg.attach(att)

    #方法
    def send_mail(self):
        try:
            # send1 = smtplib.SMTP()
            # send1.connect(self.smtpserver)
            # send1.login(self.username,self.password)
            # send1.send(self.sender,self.receiver,self.msg.as_string())
            s = smtplib.SMTP()
            s.connect(self.mail_host)
            s.login(self.mail_user, self.mail_pwd)
            s.sendmail(self.sender, self.receiver, self.msg.as_string())
            print("邮件发送成功")
        except smtplib.SMTPException as msg:
            # print(msg)
            print("Error: 无法发送邮件")
        finally:
            s.quit()


if __name__ == '__main__':
    a = configEmail()
    a.send_mail()