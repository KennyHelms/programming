import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

style.use('ggplot')

##start = dt.datetime(2019,1,1)
##end = dt.datetime(2019,12,31)
##
### df is for data frame. think of this as a spreadsheet
##
##df = web.DataReader('DJIA','yahoo', start, end)

#print(df.head(7))
#print(df.tail(7))
##df.to_csv('tesla.csv')

df = pd.read_csv('tesla.csv', parse_dates=True, index_col=0)
##print (df.head())
##df.plot()

##df['Adj Close'].plot()
##plt.show()


print (df['Adj Close'])
print (df[['Open','High']].head())
