import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
import lxml
import datetime 

index = 1

def request_tbsmend(index):
    
    today = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index-1),'%Y-%m-%d')
    yesterday = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index),'%Y-%m-%d')
    date = datetime.date.strftime(datetime.date.today()- datetime.timedelta(days=index),'%Y-%m-%d %H:%M:%S')
    print(yesterday)

    FORMURL="http://tbsnew.mand.co.kr:2189/jsp/AdminLogin.jsp"
    login_url = "http://tbsnew.mand.co.kr:2189/OperatorAction.do?cmd=login"
    stats_url = "http://tbsnew.mand.co.kr:2189/StatAction.do?cmd=statPgm&ch_key=203&start_hh=00&start_mi=00&end_hh=24&end_mi=00&start_dt={}&end_dt={}".format(yesterday,yesterday)
    payload ={
        'oper_id':'efm_24',
        'oper_pw':'8e39089c2f58b4a71aa128a9711124e5',
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
        response=s.get(stats_url).text
        soup = bs(response, 'lxml')
        #print(soup)
        tabs = pd.DataFrame({ 
                          'date':[],
                         'pgm_nm':[],
                         'rcv':[],
                         'tm':[],
                         'tmp1':[],
                         'new_sub':[],
                         'cur_sub':[],
                         'sum_sub':[] 
                        })
    
        for tr in soup.find_all('tr')[1:len(soup.find_all('tr'))-1]:
            #tds = tr.select('td')
            title =  tr.select('td')[0].text
            received =  tr.select('td')[1].text
            transmitted = tr.select('td')[2].text
            transmitperperson = tr.select('td')[3].text
            new_sub =  tr.select('td')[4].text
            cur_sub =  tr.select('td')[5].text
            sum_sub =  tr.select('td')[6].text

            insert_data = pd.DataFrame({
                'date':[date],
                'pgm_nm' : [title],
                'rcv' : [received],
                'tm' : [transmitted],
                'tmp1' : [transmitperperson],
                'new_sub' : [new_sub],
                'cur_sub' : [cur_sub],
                'sum_sub' : [sum_sub],
              
            })
    
            tabs =tabs.append(insert_data,sort=False, ignore_index=True)

    #print(tabs)
    RESULT_PATH = 'C:/1.crwaling data/mnstudio/'
    OUTPUT_FILENAME = 'efm_total_sns_{}.csv'.format(yesterday)

    tabs.to_csv(RESULT_PATH+OUTPUT_FILENAME, mode='a', header=True, index=False, encoding='utf-8') 
    #print('Created tbsnewmand_{}.csv'.format(yesterday))

request_tbsmend(1)
