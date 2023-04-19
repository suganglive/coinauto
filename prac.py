import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

def buy_market_order(self, ticker, price):

    data = {
    'market': f'{ticker}',
    'side': 'bid',
    'ord_type': 'price',
    'price': str(price),
    'volume': None
    }

    headers = self.get_header(data)

    res = requests.post(server_url + '/v1/orders', json=data, headers=headers)
    res.json()

import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

access_key = os.environ['UPBIT_OPEN_API_ACCESS_KEY']
secret_key = os.environ['UPBIT_OPEN_API_SECRET_KEY']
server_url = os.environ['UPBIT_OPEN_API_SERVER_URL']

params = {
  'market': 'KRW-BTC'
  'side': 'bid'
  'ord_type': 'limit'
  'price': '100.0'
  'volume': '0.01'
}
query_string = unquote(urlencode(params, doseq=True)).encode("utf-8")

m = hashlib.sha512()
m.update(query_string)
query_hash = m.hexdigest()

payload = {
    'access_key': access_key,
    'nonce': str(uuid.uuid4()),
    'query_hash': query_hash,
    'query_hash_alg': 'SHA512',
}

jwt_token = jwt.encode(payload, secret_key)
authorization = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization,
}

res = requests.post(server_url + '/v1/orders', json=params, headers=headers)
res.json()