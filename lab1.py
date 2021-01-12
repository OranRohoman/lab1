import requests


print(requests.__version__)
google = requests.get('https://www.google.com')
r = requests.get('https://raw.githubusercontent.com/OranRohoman/lab1/main/lab1.py')

print(r.text)
