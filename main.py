# import json
# json_text = '{"messages":[{"message":"This is the first message","timestamp":"2021-06-04 16:40:53"},{"message":"And this is a second message","timestamp":"2021-06-04 16:41:01"}]}'
# obj = json.loads(json_text)
# print(obj["messages"][1])

import requests
# Запрос без параметра
response = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.url)
print(response.status_code)

# Запрос не из списка
response = requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(response.url)
print(response.status_code)

# Запрос с правильным значением метод
response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
print(response.url)
print(response.status_code)
print(response.text)

#
methods = ["POST","GET", "DELETE", "PUT"]
for i in methods:
    for j in methods:
      if i =="POST":
        response = requests.request(i,"https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":j})
        print(i, j, response.url,  response.status_code, response.text)
      else:
        response = requests.request(i, "https://playground.learnqa.ru/ajax/api/compare_query_type",
                               data={"method": j})
        print(i, j, response.url,  response.status_code, response.text)
