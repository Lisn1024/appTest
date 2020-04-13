#导入包
import unittest,json
import time
import HTMLTestRunner
from common.Driver import Driver
from common.MyTest import MyTest
from common.readexcel import readExcel
from po.HomePage import HomePage
from po.Home_sousuo import HomeSousuo
class HomeTest(MyTest):



 #用例：首页发布微头条
    def test_weitoutiao(self):
        hp = HomePage(self.driver)
        hp.clickpublisButton()
        hp.clickwttbutton()
        hp.sendinputbutton()
        hp.clickfabubutton()
        time.sleep(3)
#搜索的测试用例（测试数据从excel中来）
    def test_sousuo(self):

        hs = HomeSousuo(self.driver)
        hs.clicksousuo()
        time.sleep(3)
        hs.sendshuru()
        time.sleep(3)
        hs.clickanniu()


    def test_sousuo1(self):


        hs = HomeSousuo(self.driver)
        hs.clicksousuo1()
        time.sleep(3)
        hs.sendshuru1()
        time.sleep(3)
        hs.clickanniu1()


    def test_sousuo2(self):

        hs = HomeSousuo(self.driver)
        hs.clicksousuo2()
        time.sleep(3)
        hs.sendshuru2()
        time.sleep(3)
        hs.clickanniu2()
#启动driver
if __name__ == '__main__':
    unittest.main()

