
from selenium.webdriver.common.by import By
class HomeSousuo(object):
    # # 定位搜索输入框
    #sousuo_button = (By.ID,"com.ss.android.article.news:id/crm")
    sousuo_button = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TabHost/android.widget.FrameLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.TextView")

    # # 定位输入内容位置
    #shuru_button = (By.ID,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/com.bytedance.android.gaia.activity.slideback.SlideFrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.EditText")
    shuru_button = (By.ID,"com.ss.android.article.news:id/csp")
    #self.driver.find_element_by_id("com.ss.android.article.news:id/csp").send_keys(text)
    # # 定位点击搜索按钮
    anniu_button = (By.ID,"com.ss.android.article.news:id/cm6")

    def __init__(self,driver):
        self.driver = driver
        # 搜索用例
        
    

    def clicksousuo(self):
        self.driver.find_element(*self.sousuo_button).click()
    def sendshuru(self):
        self.driver.find_element(*self.shuru_button).send_keys("马云")
    def clickanniu(self):
        self.driver.find_element(*self.anniu_button).click()
        
    def clicksousuo1(self):
        self.driver.find_element(*self.sousuo_button).click()
    def sendshuru1(self):
        self.driver.find_element(*self.shuru_button).send_keys("董明珠")
    def clickanniu1(self):
        self.driver.find_element(*self.anniu_button).click()
        
    def clicksousuo2(self):
        self.driver.find_element(*self.sousuo_button).click()
    def sendshuru2(self):
        self.driver.find_element(*self.shuru_button).send_keys("安卓啦贝贝")
    def clickanniu2(self):
        self.driver.find_element(*self.anniu_button).click()



    