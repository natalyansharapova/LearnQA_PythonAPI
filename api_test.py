import  requests

class TestFirstAPI:
    def test_helol(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response =requests.get(url)
        assert "HomeWork" in dict(response.cookies), "There is no field 'HomeWork' in the response"
