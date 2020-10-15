# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import pandas as pd
import re
from apscheduler.schedulers.background import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler

#네이버TV 24CH

now = datetime.now()

#tbs 김어준의 뉴스공장 네이버TV
response = requests.get("https://tv.naver.com/newsfactory")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_김어준의뉴스공장', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'newsfactory_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#팩트iN스타 (Fact in Star) 네이버TV
response = requests.get("https://tv.naver.com/tbsent1")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_팩트인스타', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbsent1_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs TV책방 북소리 네이버TV
response = requests.get("https://tv.naver.com/tvbooksori")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_TV책방북소리', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tvbooksori_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#시민의방송 tbs 네이버TV [기본채널]
response = requests.get("https://tv.naver.com/tbstv")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_시민의방송', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbstv_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 영상기록, 시간을 품다 네이버TV
response = requests.get("https://tv.naver.com/seoultime")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_영상기록', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'seoultime_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 공연에 뜨겁게 미치다 네이버TV
response = requests.get("https://tv.naver.com/crazy4stage")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_공뜨미', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'crazy4stage_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#김인권의 GOGO@무비
response = requests.get("https://tv.naver.com/gogoatmovie")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_김인권무비', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'gogoatmovie_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#홍석천의 Oh! 마이로드 네이버TV
response = requests.get("https://tv.naver.com/ohmyroad")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_오마이로드', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'ohmyroad_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 이슈파이터 네이버TV
response = requests.get("https://tv.naver.com/issuefighter")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_이슈파이터', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'issuefighter_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 상담받고 대학가자 네이버TV
response = requests.get("https://tv.naver.com/tbsmiracletv")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_기상대', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbsmiracletv_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 영화 속 숨은서울찾기 네이버TV
response = requests.get("https://tv.naver.com/movieinseoul")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_숨은서울찾기', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'movieinseoul_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 지식발전소 도시의 품격 네이버TV
response = requests.get("https://tv.naver.com/seoulcity")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_도시의품격', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'seoulcity_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#아이돌 덕후의 개똥과학 네이버TV
response = requests.get("https://tv.naver.com/gaeddong11")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_개똥과학', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'gaeddong11_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 이정렬의 품격시대 네이버TV
response = requests.get("https://tv.naver.com/tbsgrace2")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_이정렬품격시대', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbsgrace2_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#시네마 잡화점 네이버TV
response = requests.get("https://tv.naver.com/cijob")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_시네마잡화점', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'cijob_NAVERTV.csv' 
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 눈보라 유쾌한 만남 네이버TV
response = requests.get("https://tv.naver.com/tbstvradio")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_눈보라', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbstvradio_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 5분다큐 사람
response = requests.get("https://tv.naver.com/5mindocu")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_5분다큐', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = '5mindocu_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#공간사람 네이버TV
response = requests.get("https://tv.naver.com/spaceperson")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_공간사람', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'spaceperson_NAVERTV.csv' 
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#정봉주의 품격시대 네이버TV
response = requests.get("https://tv.naver.com/tbsgrace")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_정봉주품격시대', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbsgrace_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#고고학자 네이버TV
response = requests.get("https://tv.naver.com/gogohakja")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_고고학자', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'gogohakja_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs 시방 네이버TV
response = requests.get("https://tv.naver.com/sibangtbs")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_시방', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'sibangtbs_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#이니티비 네이버TV <비공개>
#response = requests.get("https://tv.naver.com/ineetv")
#soup = BeautifulSoup(response.content, 'html.parser')
#result={}
#table = soup.find_all('span', {'class':'cnt'})
#result={"ch_program":'네이버TV_이니티비', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":table[3].text, "5.total_contents":table[4].text, "6.play_list":table[5].text}
#print(result, '\n')
#RESULT_PATH ='C:/1.crwaling data/navertv/'
#OUPUT_FILENAME = 'ineetv_NAVERTV%s.csv' % (now.year)
#df = pd.DataFrame(result, index=[now])
#df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#안전지대 119 네이버TV
response = requests.get("https://tv.naver.com/safetyzone")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_안전지대 119', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'safetyzone_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")

#tbs Sports 네이버TV
response = requests.get("https://tv.naver.com/tbsfootball")
soup = BeautifulSoup(response.content, 'html.parser')
result={}
table = soup.find_all('span', {'class':'cnt'})
result={"ch_program":'네이버TV_스포츠', "1.ch_sub":table[0].text, "2.total_play":table[1].text, "3.total_like":table[2].text, "4.total_com":'-', "5.total_contents":table[3].text, "6.play_list":table[4].text}
print(result, '\n')
RESULT_PATH ='C:/1.crwaling data/navertv/'
OUPUT_FILENAME = 'tbsfootball_NAVERTV.csv'
df = pd.DataFrame(result, index=[now])
df.to_csv(RESULT_PATH+OUPUT_FILENAME, mode='a', header=False, index=True, encoding="utf-8")
