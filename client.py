import requests
import json

url = "http://127.0.0.1:8000/sum/"

payload = json.dumps({
  "int1": 1,
  "int2": 2
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)