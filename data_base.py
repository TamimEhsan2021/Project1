import psycopg2
from sqlalchemy import create_engine, engine
import pandas as pd
import os
import sqlalchemy
import configparser


class SqlDB:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('sqlconfig.ini')
        DATABASE_TYPE = config['DEFAULT']['DATABASE_TYPE']
        DBAPI = config['DEFAULT']['DBAPI']
        HOST = config['DEFAULT']['HOST']
        USER = config['DEFAULT']['USER']
        PASSWORD = config['DEFAULT']['PASSWORD']
        DATABASE = config['DEFAULT']['DATABASE']
        PORT = config['DEFAULT']['PORT']
        engine = create_engine(f"{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
        self.engine = engine
    
    def tableExists(self,table_name):
        table_exists = sqlalchemy.inspect(self.engine).has_table(table_name)

        return table_exists

    def retriveTableInfo(self,table_name):
        stock_db = pd.read_sql_table(table_name, self.engine)
        print(stock_db)
        return stock_db
    
    def createTable(self,table_name,pandas_df):
        pandas_df.to_sql(table_name, self.engine, index=False)

    def appendData(self,table_name,pandas_df):
        print(pandas_df)
        pandas_df.to_sql(table_name, self.engine, if_exists='append',index=False)
    
    def get_new_rows(self,source_df, new_df):
        """Returns just the rows from the new dataframe that differ from the source dataframe"""
        merged_df = source_df.merge(new_df, indicator=True, how='outer')
        changed_rows_df = merged_df[merged_df['_merge'] == 'right_only']

        return changed_rows_df.drop('_merge', axis=1)



