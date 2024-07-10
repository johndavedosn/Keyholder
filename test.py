import requests
import json

url = "http://192.168.8.100:8080/get-key"

data = {
    "name":"testkey",
    "token":"nicetoken"
}
headers = {
    "Content-type":"application/json"
}
res = requests.post(url, data=json.dumps(data), headers=headers).text

print(res)