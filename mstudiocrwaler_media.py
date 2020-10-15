import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import lxml
import datetime 

index = 1

pgm_key = {
    '1': '달콤한밤',
    '2': '러브레터',
    '3': '노래하는FM',
    '16': '일요클래식', 
    '522': '라디오를켜라',
    '482': '김어준 뉴스공장 주말특근',
    '483': '교통시대',
    '536': '김어준 뉴스공장',
    '549': 'tbs 아고라',
    '5': '열린아침 김만흠',
    '544': '김규리 퐁당퐁당',
    '530': '기분좋은 토요일/일요일',
    '523': '좋은사람들 송정애',
    '10': '배칠수',
    '11': '최일구',
    '548': '진짜라디오',
    '524': '이은미',
    '542': '웅산',
    '525': '김지윤',
    '526': '아닌밤중 주진우',
    '485': '주말이 좋다',
    '546': '우리동네 라디오',
    '527': '서울브루스',
    '15': '마이웨이'}

index = 1

def mediastats(pgmkey, index):
    
     # today
    
    today = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index-1),'%Y-%m-%d')
    today_mk = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index-1),'%Y-%m-%d 00:00:00')
    yesterday = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index),'%Y-%m-%d')
    date = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index),'%Y-%m-%d %H:%M:%S')
    
    #pgmkey = '536'
    #yesterday = '2019-11-05'
    #today = '2019-11-06'

    column = pd.DataFrame({
        'time' : [],
        'pgm_nm' :[],
        'media' :[],
        'rcv':[],
        'tm':[],
        'tmp1':[],
        'new_sub':[],
        'cur_sub':[],
        'sum_sub':[]
    })

    FORMURL="http://tbsnew.mand.co.kr:2189/jsp/AdminLogin.jsp"
    login_url = "http://tbsnew.mand.co.kr:2189/OperatorAction.do?cmd=login"
    #stats_url = "http://tbsnew.mand.co.kr:2189/StatAction.do?cmd=statPgm&ch_key=201&start_hh=00&start_mi=00&end_hh=24&end_mi=00&start_dt={}&end_dt={}".format(yesterday,today)
    mediastat_url = "http://tbsnew.mand.co.kr:2189/StatAction.do?cmd=statComDay&pgm_key={}&ch_key=201&start_hh=00&start_mi=00&end_hh=24&end_mi=00&start_dt={}&end_dt={}".format(pgmkey,yesterday,yesterday)
    payload ={
        'oper_id':'fm_24',
        'oper_pw':'af80d34c90c2e5511dc1af7ef2e3eab1',
        'cmd':'login',
        #'Origin':'http://tbsnew.mand.co.kr:2189',
        #'X-Requested-With':'XMLHttpRequest',
        #'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
        }
    with requests.Session() as s:
        resp = s.get(FORMURL)
        cookies = resp.cookies
        #print(resp.cookies)
        headers = requests.utils.default_headers()
        #s.headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        #login =s.post(login_url, data = payload, headers=headers, cookies=cookies)
        login =s.post(login_url, data = payload)
        #print (login.text)
        response=s.get(mediastat_url).text
        soup = bs(response, 'lxml')
        #print(soup)
        for tr in soup.find_all('tr')[1:len(soup.find_all('tr'))-1]:
            media = tr.find_all('td')[0].text
            rcv =  tr.find_all('td')[1].text
            tm = tr.find_all('td')[2].text
            tmp1 = tr.find_all('td')[3].text
            new_sub = tr.find_all('td')[4].text
            cur_sub = tr.find_all('td')[5].text
            sum_sub = tr.find_all('td')[6].text
            
            insert_data = pd.DataFrame({
                'time' : [date],
                'pgm_nm':[pgm_key.get(pgmkey)],
                'media':[media],
                'rcv':[rcv],
                'tm':[tm],
                'tmp1':[tmp1],
                'new_sub':[new_sub],
                'cur_sub':[cur_sub],
                'sum_sub':[sum_sub]
            })
            
            column =column.append(insert_data,sort=False,ignore_index=True)
            
            
    return column

index = 1
tabs = [mediastats(key,index) for key in pgm_key.keys()]
today = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index-1),'%Y-%m-%d')
yesterday = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index),'%Y-%m-%d')
result = pd.concat(tabs, ignore_index =True)
#print(result)
RESULT_PATH = 'C:/1.crwaling data/mnstudio/'
OUTPUT_FILENAME = 'fm_media_sns_{}.csv'.format(yesterday)

result.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=True, index=False, encoding='utf-8') 
