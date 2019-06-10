import requests
import json
url = 'http://data.coa.gov.tw/Service/OpenData/FromM/AgricultureiRiceFailure.aspx'

def check(json, name):
    return False


resp = requests.get(url)
if resp.status_code == 200:
    text = resp.text
    # 輸入商品名可以知道該商品是否是黑心米 ?
    json = json.loads(text)
    if check(json, '壽司米'):
        print('黑心米')
    else:
        print('安全米')
else:
    print('Error')
