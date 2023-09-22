from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import os
import time

driver = webdriver.Edge()
ac = ActionChains(driver)
driver.minimize_window()

class openPage():
    def geturl(self,url):
        driver.get(url)

if __name__ == '__main__':
    # url = 'http://mianfeizhuishu.com/3748_571418/552.html'
    with open('url.txt','r') as f:
        url = f.read()
        print(url)
    sc = openPage()
    sc.geturl(url)
    pageSource = driver.page_source
    li = driver.find_elements(by=By.CSS_SELECTOR,value='p')
    for i in li:
        print(i.text)
    x = 1
    while x == 1:
        if input()=='1':
            driver.find_element(by=By.ID,value='nextPage').click()
            pageSource = driver.page_source
            li = driver.find_elements(by=By.CSS_SELECTOR, value='p')
            for i in li:
                print(i.text)
            url = driver.current_url
            with open('url.txt','w') as f:
                f.write(url)
        else:
            x = 0
