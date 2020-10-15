# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re
from apscheduler.schedulers.background import BlockingScheduler


#tbs 팟빵 크롤링
now = datetime.now()

# Sweet Rendezvous                                 > http://www.podbbang.com/ch/1776000
response = requests.get("http://www.podbbang.com/ch/1776000")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)
subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)
hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()
drank=table3[0].text
drank=re.findall("\d+", drank)
result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)
#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1776000_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 한국어천재                                > http://www.podbbang.com/ch/1775942
response = requests.get("http://www.podbbang.com/ch/1775942")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)
subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)
hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()
drank=table3[0].text
drank=re.findall("\d+", drank)
result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)
#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775942_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 나선홍 & 최국의 맥플릭스                       > http://www.podbbang.com/ch/1775932
response = requests.get("http://www.podbbang.com/ch/1775932")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)
subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)
hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()
drank=table3[0].text
drank=re.findall("\d+", drank)
result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)
#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775932_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# K-Ride                                              > http://www.podbbang.com/ch/1775918
response = requests.get("http://www.podbbang.com/ch/1775918")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)
subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)
hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()
drank=table3[0].text
drank=re.findall("\d+", drank)
result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)
#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775918_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Uncoded                                              > http://www.podbbang.com/ch/1775917
response = requests.get("http://www.podbbang.com/ch/1775917")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)
subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)
hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()
drank=table3[0].text
drank=re.findall("\d+", drank)
result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)
#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775917_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 2020 新冠肺炎情追踪(신관폐염정추종)                     > http://www.podbbang.com/ch/1775316
response = requests.get("http://www.podbbang.com/ch/1775316")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775316_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')


# TBS eFM COVID-19 Live Updates                           > http://www.podbbang.com/ch/1775315
response = requests.get("http://www.podbbang.com/ch/1775315")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775315_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 주말이 좋다 나선홍입니다                             > http://www.podbbang.com/ch/1775174
response = requests.get("http://www.podbbang.com/ch/1775174")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1775174_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 京素一日遊(경소투어)                     > http://www.podbbang.com/ch/1774894
response = requests.get("http://www.podbbang.com/ch/1774894")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1774894_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Sunday Studio                                                 > http://www.podbbang.com/ch/1773829
response = requests.get("http://www.podbbang.com/ch/1773829")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773829_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM The Scoop                                              > http://www.podbbang.com/ch/1773641
response = requests.get("http://www.podbbang.com/ch/1773641")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773641_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')


# 슈퍼라디오 (CHN) - 历史档案(역사파일)                          > http://www.podbbang.com/ch/1773638
response = requests.get("http://www.podbbang.com/ch/1773638")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773638_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 访谈录(탐방록)                              > http://www.podbbang.com/ch/1773637
response = requests.get("http://www.podbbang.com/ch/1773637")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773637_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 温知识36.5度(지식 36.5)                     > http://www.podbbang.com/ch/1773636
response = requests.get("http://www.podbbang.com/ch/1773636")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773636_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 创业邦(창업방)                              > http://www.podbbang.com/ch/1773635
response = requests.get("http://www.podbbang.com/ch/1773635")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773635_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 优雅粉会(우아한 팬클럽)                     > http://www.podbbang.com/ch/1773634
response = requests.get("http://www.podbbang.com/ch/1773634")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773634_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 月夜体操(달밤체조)                          > http://www.podbbang.com/ch/1773633
response = requests.get("http://www.podbbang.com/ch/1773633")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773633_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 大街小巷(도시의 모든 것)                    > http://www.podbbang.com/ch/1773632
response = requests.get("http://www.podbbang.com/ch/1773632")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773632_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 测评吧8(테스트8)                            > http://www.podbbang.com/ch/1773631
response = requests.get("http://www.podbbang.com/ch/1773631")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773631_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 流行吧8(트렌드8)                            > http://www.podbbang.com/ch/1773630
response = requests.get("http://www.podbbang.com/ch/1773630")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773630_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 全民开论(열린토론)                          > http://www.podbbang.com/ch/1773629
response = requests.get("http://www.podbbang.com/ch/1773629")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773629_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 麻辣学堂(마라학당)                          > http://www.podbbang.com/ch/1773628
response = requests.get("http://www.podbbang.com/ch/1773628")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773628_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오 (CHN) - 韩语汉语 半半来(한국어반 중국어반)          > http://www.podbbang.com/ch/1773627
response = requests.get("http://www.podbbang.com/ch/1773627")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773627_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 슈퍼라디오(CHN)                                                > http://www.podbbang.com/ch/1773625
response = requests.get("http://www.podbbang.com/ch/1773625")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773625_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Super Radio                                                    > http://www.podbbang.com/ch/1773624
response = requests.get("http://www.podbbang.com/ch/1773624")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773624_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Life: Abroad                                                   > http://www.podbbang.com/ch/1773623
response = requests.get("http://www.podbbang.com/ch/1773623")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773623_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Korea, Factual                                                 > http://www.podbbang.com/ch/1773622
response = requests.get("http://www.podbbang.com/ch/1773622")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773622_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# 진짜 라디오                                                    > http://www.podbbang.com/ch/1773621
response = requests.get("http://www.podbbang.com/ch/1773621")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773621_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# TBS 아고라                                                     > http://www.podbbang.com/ch/1773620
response = requests.get("http://www.podbbang.com/ch/1773620")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773620_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 아닌 밤중에 주진우입니다                                   > http://www.podbbang.com/ch/1773615
response = requests.get("http://www.podbbang.com/ch/1773615")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773615_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 김지윤의 이브닝쇼                                          > http://www.podbbang.com/ch/1773614
response = requests.get("http://www.podbbang.com/ch/1773614")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1773614_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 색다른 시선, 김지윤입니다                                  > http://www.podbbang.com/ch/1772468
response = requests.get("http://www.podbbang.com/ch/1772468")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1772468_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 라디오를 켜라 정연주입니다                                 > http://www.podbbang.com/ch/1771190
response = requests.get("http://www.podbbang.com/ch/1771190")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1771190_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# [종영]tbs 색다른 시선, 강원국입니다                            > http://www.podbbang.com/ch/1770426
response = requests.get("http://www.podbbang.com/ch/1770426")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770426_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 偶像的品格(우상적품격)                                 > http://www.podbbang.com/ch/1770403
response = requests.get("http://www.podbbang.com/ch/1770403")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770403_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 乐动首尔(악동서울)                                     > http://www.podbbang.com/ch/1770365
response = requests.get("http://www.podbbang.com/ch/1770365")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770365_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Frenzy Friends                                         > http://www.podbbang.com/ch/1770344
response = requests.get("http://www.podbbang.com/ch/1770344")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770344_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs efm SKOOL of K-Pop                                         > http://www.podbbang.com/ch/1770343
response = requests.get("http://www.podbbang.com/ch/1770343")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770343_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 우리동네 라디오                                            > http://www.podbbang.com/ch/1770342
response = requests.get("http://www.podbbang.com/ch/1770342")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770342_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 김규리의 퐁당퐁당                                          > http://www.podbbang.com/ch/1770323
response = requests.get("http://www.podbbang.com/ch/1770323")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1770323_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Weekly Review                                          > http://www.podbbang.com/ch/1768683   
response = requests.get("http://www.podbbang.com/ch/1768683")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1768683_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Real Mom Real Talk                                     > http://www.podbbang.com/ch/1768658
response = requests.get("http://www.podbbang.com/ch/1768658")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1768658_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 10 Everyday                                            > http://www.podbbang.com/ch/1768626
response = requests.get("http://www.podbbang.com/ch/1768626")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1768626_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# Inside Korea                                                   > http://www.podbbang.com/ch/1768601
response = requests.get("http://www.podbbang.com/ch/1768601")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '1768601_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 1013信息港(1013신식항)                                 > http://www.podbbang.com/ch/16715
response = requests.get("http://www.podbbang.com/ch/16715")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '16715_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM All Things K-POP                                       > http://www.podbbang.com/ch/16367
response = requests.get("http://www.podbbang.com/ch/16367")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '16367_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# JUMPSTART                                                      > http://www.podbbang.com/ch/16339
response = requests.get("http://www.podbbang.com/ch/16339")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '16339_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 뉴스                                                       > http://www.podbbang.com/ch/16118
response = requests.get("http://www.podbbang.com/ch/16118")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '16118_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 기분좋은 토/일요일 조현아입니다.-현아스쿨,홀가분마음세탁소 > http://www.podbbang.com/ch/15495
response = requests.get("http://www.podbbang.com/ch/15495")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15495_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 김필수의 교통시대                                          > http://www.podbbang.com/ch/15381
response = requests.get("http://www.podbbang.com/ch/15381")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15381_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 周末文化走廊(주말문화주랑)                             > http://www.podbbang.com/ch/15312
response = requests.get("http://www.podbbang.com/ch/15312")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15312_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 마음산책                                                   > http://www.podbbang.com/ch/15310
response = requests.get("http://www.podbbang.com/ch/15310")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15310_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 최일구의 허리케인 라디오                                   > http://www.podbbang.com/ch/15230
response = requests.get("http://www.podbbang.com/ch/15230")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15230_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Men on Air                                             > http://www.podbbang.com/ch/15187
response = requests.get("http://www.podbbang.com/ch/15187")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '15187_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 김어준의 뉴스공장 주말특근                                 > http://www.podbbang.com/ch/14308
response = requests.get("http://www.podbbang.com/ch/14308")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '14308_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Double Date - Torn Pages                               > http://www.podbbang.com/ch/13749
response = requests.get("http://www.podbbang.com/ch/13749")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13749_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Double Date                                            > http://www.podbbang.com/ch/13748
response = requests.get("http://www.podbbang.com/ch/13748")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13748_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 首尔生活加油站(서울생활가유참)                         > http://www.podbbang.com/ch/13712
response = requests.get("http://www.podbbang.com/ch/13712")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13712_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 주말아침 박해진입니다                                      > http://www.podbbang.com/ch/13565
response = requests.get("http://www.podbbang.com/ch/13565")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13565_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM 新闻在路上(신문재로상)                                 > http://www.podbbang.com/ch/13564
response = requests.get("http://www.podbbang.com/ch/13564")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13564_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM The Steve Hatherly Show                                > http://www.podbbang.com/ch/13563
response = requests.get("http://www.podbbang.com/ch/13563")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13563_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM A Little Of A Lot                                      > http://www.podbbang.com/ch/13562
response = requests.get("http://www.podbbang.com/ch/13562")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13562_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbsFM 송정애의 좋은사람들                                      > http://www.podbbang.com/ch/13523
response = requests.get("http://www.podbbang.com/ch/13523")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13523_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# [종영]tbs 색다른 시선 - 하종강의 염치있는 세상                 > http://www.podbbang.com/ch/13353
response = requests.get("http://www.podbbang.com/ch/13353")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '13353_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# [종영]tbs 지상렬의 브라보브라보                                > http://www.podbbang.com/ch/12592
response = requests.get("http://www.podbbang.com/ch/12592")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '12592_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 김어준의 뉴스공장                                          > http://www.podbbang.com/ch/12548
response = requests.get("http://www.podbbang.com/ch/12548")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '12548_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 라디오를 켜라 김보빈입니다                                 > http://www.podbbang.com/ch/12547
response = requests.get("http://www.podbbang.com/ch/12547")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '12547_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 서울속으로 황원찬입니다                                    > http://www.podbbang.com/ch/12546
response = requests.get("http://www.podbbang.com/ch/12546")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '12546_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 가슴에 담아온 작은 목소리                                  > http://www.podbbang.com/ch/11517
response = requests.get("http://www.podbbang.com/ch/11517")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '11517_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Sounds of Korea                                        > http://www.podbbang.com/ch/11376
response = requests.get("http://www.podbbang.com/ch/11376")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '11376_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM The QUBE                                               > http://www.podbbang.com/ch/11375
response = requests.get("http://www.podbbang.com/ch/11375")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '11375_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 라디오 와이파이                                            > http://www.podbbang.com/ch/11369
response = requests.get("http://www.podbbang.com/ch/11369")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '11369_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Highlights (101.3MHz)                                  > http://www.podbbang.com/ch/11076
response = requests.get("http://www.podbbang.com/ch/11076")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '11076_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 색다른 시선, 이숙이입니다                                  > http://www.podbbang.com/ch/10135
response = requests.get("http://www.podbbang.com/ch/10135")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10135_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM The Wake Up Crew                                       > http://www.podbbang.com/ch/10122
response = requests.get("http://www.podbbang.com/ch/10122")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10122_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Koreascape                                             > http://www.podbbang.com/ch/10121
response = requests.get("http://www.podbbang.com/ch/10121")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10121_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# [정치인인터뷰] 열린아침 김만흠입니다.                          > http://www.podbbang.com/ch/10120
response = requests.get("http://www.podbbang.com/ch/10120")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10120_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 유쾌한 만남 나선홍 신보라입니다                            > http://www.podbbang.com/ch/10118
response = requests.get("http://www.podbbang.com/ch/10118")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10118_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM K-Popular with As One                                  > http://www.podbbang.com/ch/10117
response = requests.get("http://www.podbbang.com/ch/10117")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10117_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM Primetime                                              > http://www.podbbang.com/ch/10114
response = requests.get("http://www.podbbang.com/ch/10114")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10114_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM This Morning                                           > http://www.podbbang.com/ch/10101 
response = requests.get("http://www.podbbang.com/ch/10101")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10101_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs eFM The Bookend                                            > http://www.podbbang.com/ch/10095
response = requests.get("http://www.podbbang.com/ch/10095")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '10095_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')

# tbs 9595쇼_뻘전                                                > http://www.podbbang.com/ch/9611
response = requests.get("http://www.podbbang.com/ch/9611")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('dl', {'class':'likes extras'}) #좋아요
table1 = soup.find_all('dl', {'class':'subscribes extras'}) #구독
table2 = soup.find_all('dl', {'class':'ranking-hourly ranking extras'}) #카테고리 실시간
table3 = soup.find_all('dl', {'class':'ranking-daily ranking extras'}) #카테고리 일간
##정규화
like=table[0].text
like=re.findall("\d+", like)
like=",".join(like)

subs=table1[0].text
subs=re.findall("\d+", subs)
subs=",".join(subs)

hrank=table2[0].text
hrank=re.sub(re.compile(r'[\u3131-\u3163\uac00-\ud7a3]+'), '', hrank)
hrank=hrank.strip()

drank=table3[0].text
drank=re.findall("\d+", drank)

result={"1.total_like":like, "2.total_subscription":subs, "3.rank_sum":hrank}
print(result)

#SAVE FILE
RESULT_PATH = 'C:/1.crwaling data/pod/'
OUTPUT_FILENAME = '9611_PODBBANG.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=False, index=True, encoding='euc-kr')


print(now)

