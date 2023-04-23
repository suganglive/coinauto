import jwt
import hashlib
import requests
import ast
import uuid
from urllib.parse import urlencode, unquote

# ### 주문 조회 ###
# with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
#     lines = f.readlines()
#     ac = lines[1].strip()
#     se = lines[2].strip()

def get_tickers(filter='true'):
    url = f"https://api.upbit.com/v1/market/all?isDetails={filter}"
    headers = {"accept": "application/json"}
    response = requests.get(url, headers=headers)
    response = ast.literal_eval(response.text)

    krw_market_list = []
    for i in response.copy():
        if filter == 'true':
            if i['market_warning'] == 'CAUTION':
                response.remove(i)
    
    for i in response:
        if i['market'][:3] == 'KRW':
            krw_market_list.append(i['market'])
    
    return krw_market_list

class Up:
    def __init__(self, access, secret):
        self.access = access
        self.secret = secret
        self.server_url = 'https://api.upbit.com'

    def get_headers(self, data=None):
        """
        함수 이름 : get_headers
        함수 인풋 : data(optional, json 형식)
        함수 아웃풋 : headers
        함수 설명 : upbit api를 이용하기 위한 headers를 만든다.
        """
        payload = {
            'access_key': self.access,
            'nonce': str(uuid.uuid4()),
        }
        if data is not None:
            query_string = unquote(urlencode(data, doseq=True)).encode("utf-8")
            m = hashlib.sha512()
            m.update(query_string)
            query_hash = m.hexdigest()

            payload['query_hash'] = query_hash
            payload['query_hash_alg'] = "SHA512"

        jwt_token = jwt.encode(payload, self.secret, algorithm="HS256")
        authorization = 'Bearer {}'.format(jwt_token)
        headers = {
            'Authorization': authorization,
        }

        return headers

    def get_requests(self):
        """
        함수 이름 : get_rquests
        함수 인풋 : upbit api access, secret key
        함수 아웃풋 : upbit api data balance data. dictionary를 list로 감싼 형태.
        함수 설명 : upbit api를 이용해 계정의 balance data를 가져온다.
        """
        try:
            headers = self.get_headers()

            res = requests.get(self.server_url +
                               '/v1/accounts', headers=headers)
            res = res.json()
            return res
        except:
            return None

    def get_balance(self, currency):
        """
        함수 이름 : get_balance
        함수 인풋 : 얻고 싶은 화폐 이름(str) ex) "KRW", "BTC"
        함수 아웃풋 : 인풋 화폐 balance
        함수 설명 : 특정 화폐의 balance를 가져온다.
        """
        if currency != "KRW":
            currency = currency[4:]
        res = self.get_requests()
        try:
            for i in res:
                if i['currency'] == currency:
                    return float(i['balance'])
        except:
            return 0

    def buy_market_order(self, ticker, price, percentage):
        """
        함수 이름 : buy_market_order
        함수 인풋 : ticker("KRW-BTC"), price(rounded krw), percentage(float)
        함수 아웃풋 : 
        함수 설명 : 코인 시장을 시장가로 매수 주문한다.
        """
        try:
            price = price * percentage

            data = {"market": ticker,  # market ID
                    "side": "bid",  # buy
                    "price": str(price),
                    "ord_type": "price"}
            headers = self.get_headers(data)

            res = requests.post(self.server_url + '/v1/orders',
                                json=data, headers=headers)
            res.json()

        except:
            print("buy_market_order method error")

    def sell_market_order(self, ticker, volume):
        """
        함수 이름 : sell_market_order
        함수 인풋 : ticker("KRW-BTC"), volume(float)
        함수 아웃풋 : 
        함수 설명 : 코인 시장을 시장가로 매수 주문한다.
        """
        try:
            data = {"market": ticker,  # ticker
                    "side": "ask",  # sell
                    "volume": str(volume),
                    "ord_type": "market"}
            headers = self.get_headers(data)

            res = requests.post(self.server_url + '/v1/orders',
                                json=data, headers=headers)
            res.json()

        except:
            print("sell_market_order method error")


### 주문 조회 ###
with open("/Users/sugang/Desktop/school/" + "bibi.txt")as f:
    lines = f.readlines()
    ac = lines[1].strip()
    se = lines[2].strip()
