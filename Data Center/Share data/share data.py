import tushare as ts
import pandas as pd
import numpy as np
from pandas.tseries.offsets import *
sz50=ts.get_sz50s()['code'].values
np.random.shuffle(sz50)
# pd.date_range()
rng=[]

Alldata=[]
allsigma=[]
for i,stock in enumerate(sz50):
    data=ts.get_k_data(stock,start='2010-01-01', end='2017-06-02',autype=None,index=False).set_index('date')
    data = data.set_index(pd.to_datetime(data.index, format="%Y-%m-%d"))
    if(i==0):
        rng=pd.date_range('2010-01-01', '2017-06-02', freq=BDay())
        rng = pd.DataFrame(pd.Series(rng), columns=["date"]).set_index("date")

    merge=data.join(rng,how='outer')['close']
    merge=merge.ffill().bfill()
    for j in range(merge.shape[0]-1):
        merge[j]=np.log(merge[j+1]/merge[j])
    merge=merge[0:-1].values
    Alldata.append(merge)
    print(len(merge))
    if(i>0):
        matrix=np.array(Alldata)
        cov=np.cov(matrix)
        sigma=(1/(i+1))**2*np.sum(cov)
        allsigma.append(sigma)
    # rng = pd.date_range(start='7/19/2016', end='10/18/2016', freq='20min')
    # rng = pd.DataFrame(pd.Series(rng), columns=["time_window"]).set_index("time_window")
    pass
    # data.to_excel('stock of %s.xlsx' % stock)
allsigma=pd.Series(allsigma)
allsigma.to_csv('sigma4.csv')
pass