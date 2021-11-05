import string
import random
import requests
import pytest
from lib.base_case import BaseCase
from lib.assertions import Assertions
from datetime import datetime

class TestUserRegister(BaseCase):
    def setup(self):
        base_part = "learnqa"
        domain = "example.com"
        random_part = datetime.now().strftime("%m%d%Y%H%M%S")
        self.email = f"{base_part}{random_part}@{domain}"
        self.wrongemail = f"{base_part}{random_part}{domain}"
        letters = string.ascii_lowercase
        self.longname = ''.join(random.choice(letters) for i in range(250))

#Создание пользователя с очень коротким именем в один символ
    def test_create_user_neg_shortname(self):
        data = {
            'password': '123',
            'username': 'l',
            'firstName': 'learngq',
            'lastName': 'learngq',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The value of 'username' field is too short", "Unexepected content. Shoud be The value of 'username' field is too short"

#Создание пользователя с очень длинным именем - длиннее 250 символов
    def test_create_user_pos_longtname(self):
        data = {
            'password': '123',
            'username': self.longname,
            'firstName': 'learngq',
            'lastName': 'learngq',
            'email': self.email
        }
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 200)
        Assertions.assert_json_has_key(response, "id")

#Создание пользователя без указания одного из полей - с помощью @parametrize необходимо проверить,
# что отсутствие любого параметра не дает зарегистрировать пользователя
    list_data = [
        ("password", {'username': 'learnqa', 'firstName': 'learngq', 'lastName': 'learngq', 'email': 'mail@mai.ru'}),
        ("username", {'password': '123', 'firstName': 'learngq', 'lastName': 'learngq', 'email': 'mail@mai.ru'}),
        ("firstName", {'password': '123', 'username': 'learnqa', 'lastName': 'learngq', 'email': 'mail@mai.ru'}),
        ("lastName", {'password': '123', 'username': 'learnqa', 'firstName': 'learngq', 'email': 'mail@mai.ru'}),
        ("email",    {'password': '123', 'username': 'learnqa', 'firstName': 'learngq', 'lastName': 'learngq'})
    ]
    @pytest.mark.parametrize('data', list_data)
    def test_create_user_neg_without_field(self, data):
        response = requests.post("https://playground.learnqa.ru/api/user/", data=data[1])
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == f"The following required params are missed: {data[0]}", f"The following required params are missed: {data[0]}"

#Создание пользователя с некорректным email - без символа @
    def test_create_user_neg_email(self):
        data = {
            'password': '123',
            'username': 'learnqa',
            'firstName': 'learngq',
            'lastName': 'learngq',
            'email': self.wrongemail
        }

        response = requests.post("https://playground.learnqa.ru/api/user/", data=data)
        Assertions.assert_code_status(response, 400)
        assert response.content.decode("utf-8") == "Invalid email format", f"Email format is not correct {self.wrongemail}"