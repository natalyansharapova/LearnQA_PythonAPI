import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserDelete(BaseCase):
    def test_delete_user_2(self):
        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        user_id = "2"
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        Assertions.assert_code_status(response1, 200)

        # DELETE
        user_id = "2"
        response2 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Please, do not delete test users with ID 1, 2, 3, 4 or 5.", "Позволил редакировать пользовотеля из списка 1-5"

        response3 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response3, 200)

    def test_delete_user_another(self):
        data1 = self.prepare_registration_data()
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data1)
        email1 = data1["email"]
        password1 = data1["password"]
        user_id1 = self.get_json_value(response, "id")

        data2 = self.prepare_registration_data()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=data2)
        email2 = data2["email"]
        password2 = data2["password"]
        user_id2 = self.get_json_value(response2, "id")

        login_data = {
            'email': email2,
            'password': password2
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        Assertions.assert_code_status(response3, 200)

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 200)

        response5 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response5, 200)

        response6 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id1}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response6, 200)

    def test_delete_user(self):
        data = self.prepare_registration_data()
        response2 = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        email = data["email"]
        password = data["password"]
        user_id = self.get_json_value(response2, "id")

        login_data = {
            'email': email,
            'password': password
        }

        response3 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        Assertions.assert_code_status(response3, 200)

        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response4, 200)

        response5 = requests.delete(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_code_status(response5, 200)

        response6 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )

        Assertions.assert_code_status(response6, 404)
        assert response6.content.decode("utf-8") == "User not found", "Текст сообщения должен быть таким User not found"