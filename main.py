import requests
import json
import time

response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job")
obj = json.loads(response.text)
token = obj["token"]
time_left = obj["seconds"]
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
obj1 = json.loads(response.text)
if obj1["status"] == 'Job is NOT ready' :
   print("Status OK -",obj1["status"])
time.sleep(time_left)
response = requests.get("https://playground.learnqa.ru/ajax/api/longtime_job", params={"token":token})
obj1 = json.loads(response.text)
if obj1["status"] == 'Job is ready' :
   print("Status OK -",obj1["status"])