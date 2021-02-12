import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yf
import datetime as dt
from datetime import date

class ModelAnalysis():
    def __init__(self, stock_name):
        self.start_date = "2021-02-01"
        self.end_date = str(date.today())
        self.stock_name = stock_name
        self.__data = pd.DataFrame()
        
        yf.pdr_override()
        
        
    def get_stock_name(self):
        try:
            self.__data = pdr.get_data_yahoo(self.stock_name,start=self.start_date,end=self.end_date)
            self.__data.to_csv("data.csv",index=False)
        except Exception as e:
            print("exception occured")
