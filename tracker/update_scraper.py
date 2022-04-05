import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
from datetime import datetime

from sqlalchemy import create_engine
import os, requests, urllib3, time
from tracker.utils import copy_from_stringio
from dotenv import load_dotenv
import pandas as pd

HEADERS_BS = ['symbol','perct_portfolio','counts','hold_price']

HEADERS_HO = ['symbol','perct_portfolio','counts','hold_price','max_perct_portfolio']

load_dotenv()

SQLALCHEMY_DATABASE_URL=os.environ.get('DATABASE_URL')

engine = create_engine(SQLALCHEMY_DATABASE_URL)

def get_investors_act():
    investors_bs = pd.DataFrame(columns=HEADERS_BS)
    for sheet in ['b', 's']:
        for page in range(1,16):
            url = f'https://www.dataroma.com/m/g/portfolio_{sheet}.php?q=q&L={page}'
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
            response = requests.get(url, headers=headers)
            html = response.content
            q4_buys = BeautifulSoup(html,'html.parser')
            title = ''.join(q4_buys.find('p', id='p1').find_all('b')[1].text.split(' ')[::-1])
            table_headers = q4_buys.find('table', id='grid').thead.find_all('td')
            table_content = q4_buys.find('table', id='grid').tbody.find_all('tr')
            
            header_ls = []
            for td in table_headers:
                el = td.text.strip().lower().replace('▼', '').replace('*', '')
                if el == 'buys' or el == 'sells':
                    header_ls.append('counts')
                else:
                    header_ls.append(el)
            #print(header_ls)
            
            content_ls = []
            for i in range(len(table_content)):
                content_ls.append(table_content[i].find_all('td'))
            ls2 = []
            for i in content_ls:
                ls = []
                for j in i:
                    ls.append(j.text.strip().replace('$', ''))
                ls2.append(ls)
            df = pd.DataFrame(data =ls2, columns=header_ls)
            df['timing'] = title
            df['action'] = sheet
            df.rename(columns={'%': "perct_portfolio", 'hold price':'hold_price'}, inplace=True)
            df = df[['symbol','perct_portfolio','counts','hold_price', 'timing', 'action']]
            df.replace('', np.nan, inplace=True)
            df.dropna(thresh=2, inplace=True)
            df = df[df['symbol'].map(len) < 6]
            investors_bs = investors_bs.append(df, ignore_index = True)
    
    investors_bs['symbol'] = investors_bs['symbol'].str.upper()
    investors_bs['key'] = investors_bs['action'].str.upper() + investors_bs['timing'] + investors_bs['symbol']
    investors_bs = investors_bs.astype({'perct_portfolio': 'float','counts': 'float', 'hold_price': 'float'})
    
    return investors_bs

def get_investors_hold():
    investors_hold = pd.DataFrame(columns=HEADERS_BS)
    for page in range(1,16):
        url = f'https://dataroma.com/m/g/portfolio.php?pct=1&L={page}'
        headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            }
        response = requests.get(url, headers=headers)
        html = response.content
        q4_buys = BeautifulSoup(html,'html.parser')
        #title = ''.join(q4_buys.find('p', id='p1').find_all('b')[1].text.split(' ')[::-1])
        table_headers = q4_buys.find('table', id='grid').thead.find_all('td')
        table_content = q4_buys.find('table', id='grid').tbody.find_all('tr')
            
        header_ls = []
        for td in table_headers:
            el = td.text.strip().lower().replace('▼', '').replace('*', '')
            if el == 'ownershipcount':
                header_ls.append('counts')
            else:
                header_ls.append(el)
            
        content_ls = []
        for i in range(len(table_content)):
            content_ls.append(table_content[i].find_all('td'))
        ls2 = []
        for i in content_ls:
            ls = []
            for j in i:
                ls.append(j.text.strip().replace('$', ''))
            ls2.append(ls)
        df = pd.DataFrame(data =ls2, columns=header_ls)
        df['timing'] = datetime.today().strftime('%Y/%m/%d')
        #df['timing'] = title
        #df['action'] = sheet
        df.rename(columns={'%': "perct_portfolio", 'max %': 'max_perct_portfolio', 'hold price':'hold_price'}, inplace=True)
        df = df[['symbol', "perct_portfolio", 'counts', 'hold_price', 'max_perct_portfolio', 'timing']]
        df.replace('', np.nan, inplace=True)
        df.dropna(thresh=2, inplace=True)
        df = df[df['symbol'].map(len) < 6]
        investors_hold = investors_hold.append(df, ignore_index = True)
        
    investors_hold = investors_hold.astype({'perct_portfolio': 'float', 'max_perct_portfolio': 'float', 'counts': 'float', 'hold_price': 'float'})
    investors_hold['symbol'] = investors_hold['symbol'].str.upper()
    investors_hold['key'] = investors_hold['timing'] + investors_hold['symbol']
    investors_hold['max_perct_portfolio'] = investors_hold['max_perct_portfolio']/100
    investors_hold['perct_portfolio'] = investors_hold['perct_portfolio']/100
    
    return investors_hold

if __name__ == '__main__':
    copy_from_stringio(get_investors_act(), 'investors_act', engine)
    print('act done')
    copy_from_stringio(get_investors_hold(), 'investors_hold', engine)
    print('hold done')