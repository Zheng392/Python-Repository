from urllib.parse import urlencode
data = {
        'callback': 'fetchJSON_comment98vv61',
        'productId': '3555984',
        'score': 0,  # all 0 bad 1 mid 2 good 3 zhuiping 5
        'sortType': 5,  # time series rank 6 recommend rank 5
        'pageSize': 10,
        'isShadowSku': 0,
        'page': 0
    }
urlencode(data)

