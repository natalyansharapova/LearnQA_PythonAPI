import requests
from lib.base_case import BaseCase
from lib.assertions import Assertions

class TestUserEdit(BaseCase):
    def test_edit_user_put_no_auth(self):
        # EDIT
        user_id = "2"
        new_name = "Changed Name"
        response = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response, 400)

    def test_edit_user_put_auth_another_user(self):
        # LOGIN
        login_data = {
            'email': 'learnqa11062021143451@example.com',
            'password': '123'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        Assertions.assert_code_status(response1, 200)

        # EDIT
        new_name = "Changed Name"
        user_id = "2"
        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_code_status(response2, 200)

        # LOGIN
        login_data = {
            'email': 'vinkotov@example.com',
            'password': '1234'
        }
        response3 = requests.post("https://playground.learnqa.ru/api/user/login/", data=login_data)
        auth_sid = self.get_cookie(response3, "auth_sid")
        token = self.get_header(response3, "x-csrf-token")
        Assertions.assert_code_status(response3, 200)

        # GET
        response4 = requests.get(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        assert self.get_json_value(response4, "firstName") is not new_name, "Позволило изменить поле firstName для другого пользователя"

    def test_edit_user_put_wrong_email(self):
            # LOGIN
        login_data = {
            'email': 'learnqa11062021143451@example.com',
            'password': '123'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        Assertions.assert_code_status(response1, 200)

        # EDIT
        new_email = "learnqa11062021143451example.com"
        user_id = "16613"
        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"email": new_email}
        )
        Assertions.assert_code_status(response2, 400)
        assert response2.content.decode("utf-8") == "Invalid email format", "Должно быть сообщение: 'Invalid email format'"

    def test_edit_user_put_short_name(self):
        # LOGIN
        login_data = {
            'email': 'learnqa11062021143451@example.com',
            'password': '123'
        }
        response1 = requests.post("https://playground.learnqa.ru/api/user/login", data=login_data)
        auth_sid = self.get_cookie(response1, "auth_sid")
        token = self.get_header(response1, "x-csrf-token")
        Assertions.assert_code_status(response1, 200)

        # EDIT
        new_Name= "1"
        user_id = "16613"
        response2 = requests.put(
            f"https://playground.learnqa.ru/api/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_Name}
        )
        Assertions.assert_code_status(response2, 400)
        Assertions.assert_json_value_by_name(response2, "error", "Too short value for field firstName", "Некорректный текст ошибки! должен быть: 'Too short value for field firstName'")
