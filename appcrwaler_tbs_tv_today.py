from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup as bs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from apscheduler.schedulers.background import BlockingScheduler
from ast import literal_eval

import pandas as pd
import datetime
import requests
import urllib.request
import re


index=1
today = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index-1),'%Y-%m-%d')
yesterday = datetime.date.strftime(datetime.date.today()-datetime.timedelta(days=index),'%Y-%m-%d')
result={'timeMills':"timeMills",'currentEstab':"currentEstab",'dateTime':"dateTime",'dataTransferred':"dataTransferred",'bandWidth':"bandWidth"}

url = 'https://api.xtrmcdn.co.kr:28095'
traffic_stat_5sec='/api/v1/stat/apps/TID_10802/tbstv/{}'.format(today)

headers = {'X-ITX-Security-Principal':'tbs','X-ITX-Security-Secret':'0aa0c06a310921ae2a255f91ad8ddfc1f5bbade7a1910cfdf215c5ab1b3ca3c7'}
r =requests.get(url+traffic_stat_5sec, headers=headers)
res = r.text
#print(res)

result=res[180:-2]

#result=res[:180]
#print(result)

result=re.sub('":','":"', result)
result=re.sub(',"c','","c', result)
result=re.sub(',"d','","d', result)
result=re.sub(',"b','","b', result)
result=re.sub('}','"}', result)
result=re.sub('""','"', result)
result=literal_eval(result)
#print(type(result))
#print(result)

RESULT_PATH = 'C:/1.crwaling data/app/'
OUTPUT_FILENAME = 'tbs_APP_tv_{}.csv'.format(today)

df = pd.DataFrame(result)
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='w+', header=True, index=False, encoding='utf-8')
