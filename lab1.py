import requests


print(requests.__version__)

r = requests.get('https://raw.githubusercontent.com/OranRohoman/lab1/main/lab1.py')

print(r.text)
