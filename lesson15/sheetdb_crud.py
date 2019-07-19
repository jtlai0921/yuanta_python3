import requests

url = 'https://sheetdb.io/api/v1/pn0tjkupilpqk'
headers = {'Content-Type': 'application/json'}

def read():
    res = requests.get(url=url, headers=headers)
    print(res.text)

def add():
    data = '{"data":[{ "name": "Scott", "age": "21" }]}'
    res = requests.post(url=url, data=data, headers=headers)

def update():
    data = '{"data":[{ "name": "Scott", "age": "40" }]}'
    url = 'https://sheetdb.io/api/v1/pn0tjkupilpqk/name/Scott'
    res = requests.patch(url=url, data=data, headers=headers)

def delete():
    url = 'https://sheetdb.io/api/v1/pn0tjkupilpqk/name/Scott'
    res = requests.delete(url=url, headers=headers)

#add()
#update()
delete()
read()
