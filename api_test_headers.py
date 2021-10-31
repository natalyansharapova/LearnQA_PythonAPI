import  requests

class TestFirstAPI:
    def test_helol(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response =requests.get(url)
        assert "Date" in dict(response.headers), "There is no field 'Date' in the response's headers"
        assert "Content-Type" in dict(response.headers), "There is no field 'Content-Type' in the response's headers"
        assert "Content-Length" in dict(response.headers), "There is no field 'Content-Length' in the response's headers"
        assert "Connection" in dict(response.headers), "There is no field 'Connection' in the response's headers"
        assert "Keep-Alive" in dict(response.headers), "There is no field 'Keep-Alive' in the response's headers"
        assert "Server" in dict(response.headers), "There is no field 'Server' in the response's headers"
        assert "x-secret-homework-header" in dict(response.headers), "There is no field 'x-secret-homework-header' in the response's headers"
        assert "Cache-Control" in dict(response.headers), "There is no field 'Cache-Control' in the response's headers"
        assert "Expires" in dict(response.headers), "There is no field 'Expires' in the response's headers"



