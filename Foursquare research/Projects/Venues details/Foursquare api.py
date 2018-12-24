'''
#test the search function
import json, requests
url = 'https://api.foursquare.com/v2/venues/search'

params = dict(
  client_id='5MDTT4NQVXV3VQF3KEA50Z2T0DLQ5TJAF1C2UVERXOJD5V4E',
  client_secret='QK4AM22AD13GNIMNJLSHGEFX5VPBPH3JALD50L3P3CHBYHQF',
  v='20180323',
  ll='37.756803, -122.429917',
  radius=100000,
  intent='browse',
  limit=20
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)

'''

#test explore
'''
import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
  client_id='5MDTT4NQVXV3VQF3KEA50Z2T0DLQ5TJAF1C2UVERXOJD5V4E',
  client_secret='QK4AM22AD13GNIMNJLSHGEFX5VPBPH3JALD50L3P3CHBYHQF',
  near='San Francisco, CA',
  v='20180323',
  radius=100000,
offset='100000',
  limit='50',
  time='any',
  day='any',
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(resp.text)
'''

# #test venue's photo
# import json, requests
# url = 'https://api.foursquare.com/v2/venues/445e36bff964a520fb321fe3/photos'
#
# params = dict(
#   client_id='5MDTT4NQVXV3VQF3KEA50Z2T0DLQ5TJAF1C2UVERXOJD5V4E',
#   client_secret='QK4AM22AD13GNIMNJLSHGEFX5VPBPH3JALD50L3P3CHBYHQF',
#   v='20180323',
#   limit='500',
#
# )
# resp = requests.get(url=url, params=params)
# data = json.loads(resp.text)
# with open('Foursquare api test result.txt','w') as f:
#   f.write(resp.text)


# test venue's tips
# import json, requests
# url = 'https://api.foursquare.com/v2/venues/445e36bff964a520fb321fe3/tips'

# params = dict(
#   client_id='5MDTT4NQVXV3VQF3KEA50Z2T0DLQ5TJAF1C2UVERXOJD5V4E',
#   client_secret='QK4AM22AD13GNIMNJLSHGEFX5VPBPH3JALD50L3P3CHBYHQF',
#   v='20180323',
#   sort='popular',
#   limit=500,
#   offset=200,

# )
# resp = requests.get(url=url, params=params)
# data = json.loads(resp.text)
# with open('Foursquare api test result.txt','w') as f:
#   m=json.dumps(data)
#   f.write(m)
# print(resp.text)
# with open('Foursquare api test result.txt','w') as f:
#   f.write(resp.text)

# test venue's categories
import json, requests
url = 'https://api.foursquare.com/v2/venues/categories'


params = dict(
  client_id='5MDTT4NQVXV3VQF3KEA50Z2T0DLQ5TJAF1C2UVERXOJD5V4E',
  client_secret='QK4AM22AD13GNIMNJLSHGEFX5VPBPH3JALD50L3P3CHBYHQF',
  v='20180323'

)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)
print(data)
with open('Categories.json','w') as f:
  json.dump(data,f)

#   f.write(m)
# print(resp.text)