
from selenium.webdriver.common.by import By
class HomePage(object):

#发微头条用例
    #点击发布按钮
    publish_button = (By.ID,"com.ss.android.article.news:id/byg")
    #点击发微头条
    wtt_button = (By.XPATH,"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.ImageView")
   #点击输入框输入微头条内容
    input_button = (By.ID,"com.ss.android.article.news:id/a8j")
    #点击发布微头条
    fabu_button = (By.ID,"com.ss.android.article.news:id/cm4")


   

    def __init__(self,driver):
        self.driver = driver

    def clickpublisButton(self):
        self.driver.find_element(*self.publish_button).click()
    def clickwttbutton(self):
        self.driver.find_element(*self.wtt_button).click()
    def sendinputbutton(self):
        self.driver.find_element(*self.input_button).send_keys("我要发微博，哈哈哈哈……")
    def clickfabubutton(self):
        self.driver.find_element(*self.fabu_button).click()

   



