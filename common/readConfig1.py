'''
1-导入包
2-创建对象
3-读取内容
4-关闭
'''
import os

import configparser

class ReadConfig(object):
    def __init__(self):
        self.cf = configparser.ConfigParser()
        #建议使用绝对路径，使用相对路径，在runall中调用程序找不到config.txt文件
        #self.cf.read(r'..\config1.txt', encoding="utf-8-sig")
        self.cf.read(r'E:\code\person\appTest\venv\config1.txt', encoding="utf-8-sig")
#获取单个数据
    def get_email(self,canshu):
        return self.cf.get("EMAIL",canshu)

#一次获取全部数据
    def get_emailall(self):
        return self.cf.items("EMAIL")


if __name__ == '__main__':
    re = ReadConfig()
    print(re.get_emailall())
    print(re.get_email('mail_user'))