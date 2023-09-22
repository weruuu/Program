from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Edge()
ac = ActionChains(driver)
driver.maximize_window()

class openPage():
    def geturl(self,url):
        driver.get(url)

    def actClick(self,reset,xpath):
        try:
            element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, xpath)))
            ac.move_to_element(element).perform()
            element.click()
            print('success')
        except:
            print('error')
        time.sleep(0.2)
        if reset == 1:
            ac.move_by_offset(1,1)  #释放当前激活元素

    def inputBox(self,type,value,text):
        if type == 'id':
            element = driver.find_element(by=By.ID,value=value)
            element.send_keys(text)
        elif type == 'xpath':
            element = driver.find_element(by=By.XPATH,value=value)
            element.send_keys(text)

        time.sleep(0.2)
        ac.move_by_offset(1,1).click().perform()  #释放当前激活元素

    def login(self,passport,password):
        passport_text = driver.find_element(by=By.NAME, value="passport")
        password_text = driver.find_element(by=By.NAME, value="password")
        submit_button = driver.find_element(by=By.XPATH,value="/html/body/form/div/div/div[3]/button[1]")
        passport_text.send_keys(passport)
        password_text.send_keys(password)
        submit_button.click()

    def createKunnr(self):
        element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id=\"navigation_3\"]/a')))
        element.click()

        time.sleep(1)
        ac.move_by_offset(1,1).click().perform()  #释放当前激活元素
        time.sleep(1)

        # XPATH查询方法
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id=\"rootTree\"]/li[1]/div')))
        element.click()

        # selector查询方法
        element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#rootTree > li:nth-child(1) > ul > li:nth-child(2) > div')))
        element.click()

    def fillframe(self):

        # 进入iframe
        iframe = driver.find_element(by=By.XPATH,value="//*[@id=\"tabs\"]/div[2]/div[2]/div/iframe")
        driver.switch_to.frame(iframe)

        # 选择开户类型
        # @method
        self.actClick(0,'//*[@id=\"ff\"]/div[1]/div[2]/table/tbody/tr[2]/td[2]/span')
        self.actClick(1,'/html/body/div[27]/div/div[1]')

        # 经销商名称
        self.inputBox('id','name1','测试经销商')

        # 行政城市
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[2]/td[8]/span/span/span')
        self.actClick(1,'//*[@id="datagrid-row-r6-2-0"]/td/div')

        # 经销商类型
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[3]/td[4]/span')
        self.actClick(1,'/html/body/div[2]/div/div[2]')

        # 经营模式
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[3]/td[6]/span')
        self.actClick(1,'/html/body/div[26]/div/div[1]')

        # 经营品牌
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[4]/td[2]/span')
        self.actClick(0,'/html/body/div[3]/div/div[1]')
        self.actClick(0,'/html/body/div[3]/div/div[2]')

        # 经营品类
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[4]/td[4]/span')
        self.actClick(0,'/html/body/div[4]/div/div[1]')
        self.actClick(1,'/html/body/div[4]/div/div[2]')

        # 经营小类
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[4]/td[6]/span/input')
        self.actClick(0,'//*[@id="datagrid-row-r5-2-0"]')
        self.actClick(1,'//*[@id="datagrid-row-r5-2-1"]')

        # 是否新开
        self.actClick(0,'//*[@id="ff"]/div[2]/div[2]/table/tbody/tr[5]/td[2]/span')
        self.actClick(1,'/html/body/div[5]/div/div[1]')

if __name__ == '__main__':
    url = 'http://exp.zjxpp.com:8186/basisPlatform/'
    sc = openPage()
    sc.geturl(url)
    sc.login('admin','52Xpp@2022')
    time.sleep(2)
    sc.createKunnr()
    sc.fillframe()
    #新建标签页
    # js = "window.open('{}','_blank');"
    # driver.execute_script(js.format('https://www.baidu.com'))

time.sleep(5000)
driver.quit()