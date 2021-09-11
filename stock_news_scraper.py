from pandas import pandas as pd 
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.request import Request
import time # You are not using this library
import datetime # You are not using datetime
import pandas as pd
from collections import defaultdict # You are not using defauldict
from tqdm import tqdm


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()

obj = SentimentIntensityAnalyzer()


class StockScraper:
    def __init__(self):
        pass


    def snpCompanies(self):
        tickers = []
        table=pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
        snp_df = table[0]
        symbol = snp_df['Symbol']
        for ticker in symbol:
            tickers.append(ticker)
        return tickers


    def stockContent(self, tickers):


        dict_name = ['ticker','stock_name','stock_sector','stock_type','stock_region','stock_info']
        stock_data = {}
        for i in range(len(dict_name)):
            stock_data[dict_name[i]] = []


        try:
            for ticker in tqdm(tickers):
                print("processing", ticker)
                if "." in ticker:
                    ticker = ticker.replace(".","-")
                finviz_url = 'https://finviz.com/quote.ashx?t='
                news_tables = {}
                url = finviz_url + ticker
                req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'})
                resp = urlopen(req)
                html = BeautifulSoup(resp, features="lxml")
                stock_name = html.find_all('a', {'class':'tab-link'})[12].text
                stock_sector= html.find_all('a', {'class':'tab-link'})[13].text
                stock_type= html.find_all('a', {'class':'tab-link'})[14].text
                stock_region= html.find_all('a', {'class':'tab-link'})[15].text
                stock_info= html.find('td', {'class':'fullview-profile'}).text

                stock_value = [ticker,stock_name,stock_sector,stock_type,stock_region,stock_info]

                for i in range(len(stock_value)):
                     stock_data[dict_name[i]].append(stock_value[i])

            df = pd.DataFrame.from_dict(stock_data)          
            return df
        except Exception as e:
            print(e)

    
    def getNewsHeadlines(self, tickers):
        dict_name = ['ticker','headline','date']

        headline_data = {}
        for i in range(len(dict_name)):
            headline_data[dict_name[i]] = []
        try:
            for ticker in tqdm(tickers):
                print("processing", ticker)
                if "." in ticker:
                    ticker = ticker.replace(".","-")

                finviz_url = 'https://finviz.com/quote.ashx?t='
                news_tables = {}
                url = finviz_url + ticker
                req = Request(url=url,headers={'user-agent': 'my-app/0.0.1'})
                resp = urlopen(req)
                html = BeautifulSoup(resp, features="lxml")
                n=100
                news_tables = html.find(id='news-table')
                news_tables[ticker] = news_tables
                df = news_tables[ticker]
                df_tr = df.findAll('tr')
                for i, table_row in enumerate(df_tr):
                    article_headline = table_row.a.text
                    td_text = table_row.td.text
                    article_date = td_text.strip()
                    headline_value = [ticker,article_headline,article_date]

                    for i in range(len(headline_value)):
                        headline_data[dict_name[i]].append(headline_value[i])
                
                    if i == n-1:
                        break
            df = pd.DataFrame.from_dict(headline_data)    
            return df

        except Exception as e:
            print(e)
    


    def getTwiterData(self):
        try:
            pass
        
        except Exception as e:
            print(e)


  