import tushare as ts
sz50=ts.get_sz50s()['code'].values
# for stock in sz50:
#     data = ts.get_k_data(stock, start='2010-01-01', end='2017-06-02', autype=None, index=False,ktype='M')
#     data.to_excel('Month data/stock of %s.xlsx' % stock)
#     pass
stock='000016'
data = ts.get_k_data(stock, start='2010-01-01', end='2017-06-02', autype=None, index=True,ktype='M')
data.to_excel('Month data/stock of %s.xlsx' % stock)