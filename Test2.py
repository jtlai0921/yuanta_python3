
import requests

url = 'https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.gz'

r = requests.get(url)

print(r.text)
