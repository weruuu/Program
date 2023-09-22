from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

def get_track(distance):      # distance为传入的总距离
    track = [] # 移动轨迹
    current = 0 # 当前位移
    mid = distance * 4/5 # 减速阈值
    t = 2 # 计算间隔
    v = 1 # 初速度
    while current<distance:
        if current<mid:
            a=5 # 加速度为2
        else:
            a=-3 # 加速度为-2
        v0 = v
        v= v0 + a * t # 当前速度
        move = v0 * t + 1/2 * a * t * t # 移动距离
        current += move # 当前位移
        track.append(round(move)) # 加入轨迹
        # print(track)
    return track

def move_to_gap(slider,tracks):     # slider是要移动的滑块,tracks是要传入的移动轨迹
    ActionChains(driver).click_and_hold(slider).perform()
    for x in tracks:
        ActionChains(driver).move_by_offset(xoffset=x,yoffset=0).perform()
    time.sleep(0.5)
    ActionChains(driver).release().perform()

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

id_list = []
area = '卧龙区'
key_word = '便利'
index,count = 1,1

driver.get("https://ditu.amap.com/")
time.sleep(2)
driver.find_element(by=By.XPATH, value="/html/body/section[1]/header/div[2]/input").send_keys(area)
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/section[1]/header/div[2]/div/i").click()
time.sleep(5)
try:
    print('try to find')
    driver.switch_to.frame("baxia-dialog-content")
    # driver.switch_to.frame("iframeResult")
    slide_box = driver.find_element(by=By.ID, value="nc_1_n1z")
    # slide_box = driver.find_element(by=By.ID, value="draggable")
    print('find!')
    move_to_gap(slide_box, get_track(310))
except:
    1 == 1
driver.find_element(by=By.XPATH, value="/html/body/section[1]/header/div[2]/input").send_keys(key_word)
time.sleep(1)
driver.find_element(by=By.XPATH, value="/html/body/section[1]/header/div[2]/div/i").click()
time.sleep(2)

ele = driver.find_element(by=By.XPATH, value= "/html/body/div[1]/section/section/div[1]/ul")
driver.execute_script('document.getElementById("serp").scrollTop = 10000', ele)
page_num = driver.find_element(by=By.XPATH, value= "/html/body/div[1]/section/section/div[2]/b").text
page_num = int(page_num[page_num.find('/')+1:page_num.find('页')])
print('共'+str(page_num)+'页')
while index <= page_num:
    time.sleep(2)
    try:
        print('try to find')
        driver.switch_to.frame("baxia-dialog-content")
        # driver.switch_to.frame("iframeResult")
        slide_box = driver.find_element(by=By.ID, value="nc_1_n1z")
        # slide_box = driver.find_element(by=By.ID, value="draggable")
        print('find!')
        move_to_gap(slide_box, get_track(310))
    except:
        1 == 1
    try:
        ele = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/section/div[1]/ul")
        driver.execute_script('document.getElementById("serp").scrollTop = 10000', ele)
        ul = driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/section/div[1]/ul")
        li_name = ul.find_elements(by=By.TAG_NAME, value="li")
        for i in li_name:
            id_list.append(i.get_attribute("id"))
            print(count,i.get_attribute("id"))
            count += 1
        driver.find_element(by=By.XPATH, value="/html/body/div[1]/section/section/div[2]/span[1]/i").click()
    except:
        1 == 1
    index += 1
for j in id_list:

    name,addr,tel = '','',''
    # print(j)
    url = 'https://ditu.amap.com/place/'+j
    driver.get(url)
    time.sleep(2)
    try:
        name = driver.find_element(by=By.XPATH, value="/html/body/section[2]/div/section/div/div[4]/div/section[1]/h3").text
    except:
        name = ''
    try:
        addr = driver.find_element(by=By.XPATH, value="/html/body/section[2]/div/section/div/div[4]/div/ul/li[1]/p").text
    except:
        addr = ''
    try:
        tel = driver.find_element(by=By.XPATH, value="/html/body/section[2]/div/section/div/div[4]/div/ul/li[2]/p").text
    except:
        tel = ''
    print(name,addr,tel)
#滑块
#
# try:
#     driver.find_element(by=By.XPATH, value= "/html/body/div[1]/section/section/div[2]/span[1]/i").click()
# except:
#     exit()

#
# driver.get("https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=11&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10.48&city=420600&geoobj=111.062111%7C31.28742%7C112.482819%7C32.0256&keywords=%E4%BE%BF%E5%88%A9")
#
# html = driver.page_source
# start = html.find('poi_list')
# end = html.find('SPQ')
# text = '{"'+html[start:end-2]
# print(text)
#
# data = json.loads(text)
# get = data['poi_list']
# i = 1
# for item in get:
#     name, tel, address = '', '', ''
#     if item['name'] == '':
#         name = '|'
#     else :
#         name = item['name']
#     if item['tel'] == '':
#         tel = '|'
#     else :
#         tel = item['tel']
#     if item['address'] == '':
#         address = '|'
#     else :
#         address = item['address']
#     print(i,name,tel,address)
#     i+=1

# driver.get("https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=4&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10.48&city=420600&geoobj=111.062111%7C31.28742%7C112.482819%7C32.0256&keywords=%E4%BE%BF%E5%88%A9")  # 打开网址
# driver.maximize_window()  # 窗口最大化（无关紧要哈）
