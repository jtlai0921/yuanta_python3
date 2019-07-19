import requests

url = 'https://sheetdb.io/api/v1/pn0tjkupilpqk'
headers = {'Content-Type': 'application/json'}

def read():
    res = requests.get(url=url, headers=headers)
    print(res.text)

read()
