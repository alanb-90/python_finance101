import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt 
from pandas_datareader import data as pdr


yf.pdr_override()

stock = input("Enter a stock ticker symbol: ")

print(stock)

startyear = 2019
startmonth = 1
startday = 1

start = dt.datetime(startyear, startmonth, startday)

now = dt.datetime.now()

df = pdr.get_data_yahoo(stock, start, now)

#moving average
ma = 50
smaString = "Sma_"+str(ma)

#Creating column with Smastring, the rolling moving average with window size of 50  ----4th column within DF ----
df[smaString] = df.iloc[:,4].rolling(window = ma).mean()

df = df.iloc[ma:]

#Prints all moving averages
# for i in df.index:
#     print(df[smaString][i])

numH = 0
numC = 0

for i in df.index:
    if(df['Adj Close'][i] > df[smaString][i]):
        print('The Close is higher')
        numH +=1
    else:
        print("The Close is lower")
        numC +=1

print(str(numH))
print(str(numC))