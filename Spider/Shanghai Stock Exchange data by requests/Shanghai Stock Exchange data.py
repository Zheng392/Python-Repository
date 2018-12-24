import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',\
          'Referer': 'http: // www.sse.com.cn / disclosure / dealinstruc / suspension /'
}
payload = {'jsonCallBack': 'vajsonpCallback68485', 'isPagination': 'true', 'bgFlag': '1', \
            'pageHelp.pageNo': '1', 'pageHelp.beginPage': '1'}
params={"isPagination": 'true','searchDate': "",'bgFlag': 1,
'searchDo': 1,\
"pageHelp.pageSize": 1500,\
"pageHelp.pageNo": 1,\
"pageHelp.beginPage": 1,\
"pageHelp.cacheSize": 1,\
"pageHelp.endPage": 3,\
'desc':"",\
'pageCache':1
}
r=requests.get(url='http://query.sse.com.cn/infodisplay/querySpecialTipsInfoByPage.do',params=params,headers=headers)
print(r.headers)
print(r.json())
pass