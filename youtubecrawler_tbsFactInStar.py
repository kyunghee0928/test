from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.background import BlockingScheduler

import pandas as pd
import time
import requests
import urllib.request
import re
'''
chrome_options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
chrome_options.add_argument('headless') # headless 모드 설정
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('lang=ko_KR')
'''

driver = webdriver.Chrome('C:/chromedriver.exe')
driver.get("https://www.youtube.com/")
driver.maximize_window()

driver.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()
time.sleep(2)

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys('kyunghee0928@gmail.com')
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys('!rhrudgml8290')
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="avatar-btn"]').click()
time.sleep(5)

driver.find_element_by_xpath('//*[@id="items"]/ytd-compact-link-renderer[4]').click()
time.sleep(5)


driver.find_element_by_xpath('/html/body/ytd-app/ytd-popup-container/iron-dropdown/div/ytd-multi-page-menu-renderer/div[4]/ytd-multi-page-menu-renderer/div[3]/div[1]/ytd-account-section-list-renderer/div/ytd-account-item-section-renderer/div/ytd-account-item-renderer[4]').click()
time.sleep(5)


driver.find_element_by_xpath('//*[@id="avatar-btn"]').click()
time.sleep(5)


driver.find_element_by_xpath('//*[@id="items"]/ytd-compact-link-renderer[3]').click()
time.sleep(5)

now = datetime.now()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
#print(soup)
subs = soup.find('div', {'class':'metric-value-big style-scope ytcd-channel-facts-item'})
print(subs.text.strip(), now)

result = {"subscription":subs.text.strip(), "ch":'tbsFactInStar'}

RESULT_PATH = 'C:/1.crwaling data/youtube/'
OUTPUT_FILENAME = 'tbsFactInStar_YOUTUBE.csv'

df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='utf-8')

print("크롤링 완료", now)

driver.close()
