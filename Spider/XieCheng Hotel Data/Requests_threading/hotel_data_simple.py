import requests
import json

headers = {'Referer': 'http://hotels.ctrip.com/hotel/shanghai2','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36'}

for i in range(1,384):
	data={'page':i,'cityPY':'shanghai','cityId':2,'cityCode':'021' }
	r = requests.post('https://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx', data = data, headers=headers)
	print(r.text)
	print(i)

pass



#
# headers = {'Referer': 'http://hotels.ctrip.com/hotel/shanghai2',}
#
# for i in range(1000):
# 	data={'page':i,'cityPY':'shanghai','cityId':2,'cityCode':'021' }
# 	r = requests.post('http://hotels.ctrip.com/Domestic/Tool/AjaxHotelList.aspx', data = data, headers=headers)
# 	print(r.text)
# 	print(i)
#
# pass