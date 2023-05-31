import pandas as pd
import requests
import json


api_key = "rA59CeDrWCmc5r_rB1PnGo50T2Jxt7bsZgA0UcvsqBid7qlXCEienAB6J_JNZMSNMAwqpQAmCEVaYqgTLzHYGl86IIyYl-BA2M4ZkV4UuWC_oWST667Y8bKtP2x1ZHYx"

headers = {'Authorization': 'Bearer %s' % api_key}

# Yelp Business Search API

url='https://api.yelp.com/v3/businesses/search'
params = {'term':'restaurant','location':'Houston','limit':50}

req = requests.get(url, params=params, headers=headers)
print('The status code is {}'.format(req.status_code))

result = json.loads(req.text)

# Convert the result to a dataframe
df = pd.DataFrame(result['businesses'])

print(df.shape)
df.to_csv('yelp_businesses.csv', index=False)