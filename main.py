from stock_news_scraper import StockScraper
from data_base import SqlDB
import pandas as pd
from Sentiment_analysis import sentimentAnalysis

# Declaring datatable names
dt_stockContent = "stock_content"
dt_headlines = "stock_headlines"
dt_sentiment = "stock_sentiment"

#configuing stockscraper because it is a class
config_stock = StockScraper()
config_sql = SqlDB()

def addStockSqlData(dt_stockContent,updateFlag):
    # config_sql = SqlDB()
    '''
    Add stock info to sql data base
    Checks if stock info table exists
    Creates new table if table does not exist
    Checks if an update is required
    Uses the same table if update is not required
    '''
    stock_col = ['ticker','stock_name','stock_sector','stock_type','stock_region','stock_info']
    df = pd.DataFrame(columns=stock_col)
    content = df

    table_exists = config_sql.tableExists(table_name=dt_stockContent)
    if table_exists == True:
        print("data base exists")
        retrieve_table = config_sql.retriveTableInfo(table_name=dt_stockContent)
        
        if updateFlag == True:
            stock_list = config_stock.snpCompanies()
            content = config_stock.stockContent(tickers=stock_list)
        else:
            stock_list = ["TSLA","F"]
            content = config_stock.stockContent(tickers=stock_list)

        new_dt = config_sql.get_new_rows(source_df=retrieve_table, new_df=content)

        config_sql.appendData(table_name=dt_stockContent, pandas_df=new_dt)
    else:
        create_table = config_sql.createTable(table_name=dt_stockContent, pandas_df=content)
        print("create data table:",dt_stockContent)


def addHeadlinesSqlData(stockInfo_dt,updateFlag,headline_dt):
        config_sql = SqlDB()
        
        headline_tableExists = config_sql.tableExists(table_name=headline_dt)
        if headline_tableExists == True:
            print("data base exists")
            retrieve_headline_table = config_sql.retriveTableInfo(table_name=headline_dt)
            if updateFlag == True:
                retrieve_stock_info = config_sql.retriveTableInfo(table_name=stockInfo_dt)
                dt_tickers = retrieve_stock_info['ticker'].tolist()
                new_dt=config_stock.getNewsHeadlines(dt_tickers)
                original_dt = retrieve_headline_table

            else:
                new_dt = retrieve_headline_table
                original_dt = retrieve_headline_table

            append_dt = config_sql.get_new_rows(source_df=original_dt, new_df=new_dt)

            config_sql.appendData(table_name=headline_dt, pandas_df=append_dt)
        else:

            headline_col = ['ticker', 'headline', 'date']

            df = pd.DataFrame(columns=headline_col)
            create_table = config_sql.createTable(table_name=headline_dt, pandas_df=df)
            print("created data table:",headline_dt)

def sentimentSqlData(sentiment_dt, updateFlag, headline_dt):
    sentiment_col = ['date','ticker','headline','sentiment']
    content = pd.DataFrame(columns=sentiment_col)
    sentiment_tableExists = config_sql.tableExists(table_name=sentiment_dt)
    if sentiment_tableExists == True:
        retrieve_sentiment_table = config_sql.retriveTableInfo(table_name=sentiment_dt)
        if updateFlag == True:
            retrieve_headline_table = config_sql.retriveTableInfo(table_name=headline_dt)
            dt_tickers = retrieve_headline_table['ticker'].tolist()
            dt_headlines = retrieve_headline_table['headline'].tolist()
            dt_date = retrieve_headline_table['date'].tolist()
            new_dt=sentimentAnalysis(ticker=dt_tickers, headlines=dt_headlines, date=dt_date)
            print(type(new_dt))
            print(type(retrieve_sentiment_table))
            append_dt = config_sql.get_new_rows(source_df=retrieve_sentiment_table, new_df=new_dt)
            print("Retrieve data", retrieve_sentiment_table)
            print("This is append", append_dt)
            config_sql.appendData(table_name=sentiment_dt, pandas_df=append_dt)

    else:
        create_table = config_sql.createTable(table_name=sentiment_dt, pandas_df=content) 




# addStockSqlData(dt_stockContent=dt_stockContent, updateFlag=True)
# addHeadlinesSqlData(headline_dt = dt_headlines, stockInfo_dt = dt_stockContent, updateFlag = True)
sentimentSqlData(sentiment_dt=dt_sentiment, updateFlag=True, headline_dt=dt_headlines)

# addStockSqlData(dt = dt_stockContent,updateFlag = False)
# config_sql = SqlDB()
# retrieve_table = config_sql.retriveTableInfo(table_name=dt_stockContent)
# dt_tickers = retrieve_table['ticker'].tolist()

# # get_news_headlines = config_stock.getNewsHeadlines(tickers = dt_tickers)
# # print(get_news_headlines)
# addSqlData(dt = dt_headlines,updateFlag = False)

