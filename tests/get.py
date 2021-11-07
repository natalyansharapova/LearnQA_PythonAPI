import requests

class TestFirstAPI:
    def test_get(self):
        response = requests.get("https://playground.learnqa.ru/api/get_text")
        print(response.content)
