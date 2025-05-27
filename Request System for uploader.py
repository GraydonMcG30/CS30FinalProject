import requests

url = "http://127.0.0.1:5000/upload"
files = {'file': open('/Users/djangod/text.txt', 'rb')}
r = requests.post(url, files=files)