from common.readConfig1 import ReadConfig
class configEmail(object):
    def __init__(self):
        re = ReadConfig
        conf_list = re.get_emailall()
        self.mail_user = conf_list[1][1]

if __name__ == '__main__':
    a = configEmail


