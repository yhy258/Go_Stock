from bs4 import BeautifulSoup
import requests
import json
"""
    해외 주식만..
    에잉.. 그냥 url 뚜들겨서 조회하면 안나온다.
"""
base_url = "https://api.stock.naver.com/stock/"
NASDAQ = True
CODE = "AAPL" # 애플!
if NASDAQ :
    url = base_url + CODE + '.O/basic' # 네트워크에서 불러오는 부분이라서 "network response"보면서 찾아줘야한다.

response = requests.get(url)

if response.status_code == 200:
    html = response.text # 해당 페이지 가져옴
    bsObj = BeautifulSoup(html, 'html.parser')
    jsonObj = json.loads(str(bsObj))
    print(jsonObj)
"""
    'stockExchangeType' : 'code', 'startTime', 'endTime' 
    'closePrice'
    ... 
"""
print(jsonObj['closePrice'])
