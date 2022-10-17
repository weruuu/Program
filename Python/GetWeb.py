# import asyncio
# from pyppeteer import launch
#
# async def main():
#     browser = await launch(headless=False, args=['--disable-infobars','--window-size=1920,1080'])
#     page = await browser.newPage()
#     await page.setViewport({'width': 1920, 'height': 1080})
#     await page.setUserAgent(
#         "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/71.0.3542.0 Safari/536.5")
#     await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
#     await page.goto('')
#     page_text = await page.content()  # 获取网页源码
#     print(page_text)
#     await asyncio.sleep(500)
#
# asyncio.get_event_loop().run_until_complete(main())
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
# options = webdriver.ChromeOptions()
# 配置
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# options.add_argument('--blink-settings=imagesEnabled=false');#无图模式

# options.add_argument("--disable-blink-features")
# options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument('--incognito')#无痕模式
# options.add_argument("--disable-extensions")
# options.add_argument("--disable-infobars")
# options.add_argument("--no-default-browser-check")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option("useAutomationExtension", False)
# chromedriver = "C:/Program Files/Google/Chrome/Application/chromedriver"

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)

# os.environ["webdriver.chrome.driver"] = chromedriver
# driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
driver.get("https://ditu.amap.com/search?query=%E4%BE%BF%E5%88%A9&city=420600&geoobj=111.062111%7C31.28742%7C112.482819%7C32.0256&zoom=10.48&pagenum=3")
driver.execute_script("window.open();")  # 注意js语句要带分号
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[1])  # 假设此时只有两个窗口，那么就切换到了第二个窗口
driver.get("https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=3&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10.48&city=420600&geoobj=111.062111%7")
print(driver.page_source)

# driver.get("https://ditu.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=4&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=10.48&city=420600&geoobj=111.062111%7C31.28742%7C112.482819%7C32.0256&keywords=%E4%BE%BF%E5%88%A9")  # 打开网址
driver.maximize_window()  # 窗口最大化（无关紧要哈）


