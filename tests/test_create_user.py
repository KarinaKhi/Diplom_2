from conftest import *
import allure
from data import USER_DATA_FOR_LOGIN


@allure.feature("Создание пользователя")
class TestCreateUser:

    @allure.title('Проверка успешного создания уникального пользователя')
    def test_create_unique_user(self, user_methods, random_user_data):
        status_code, response_data = user_methods.register_user(random_user_data)
        assert status_code == 200 and response_data.get("success") is True and "accessToken" in response_data, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.story('Создание пользователя с уже существующими данными')
    def test_create_user_already_registered(self, user_methods):
        already_registered_user = {
            "email": USER_DATA_FOR_LOGIN["email"],
            "password": USER_DATA_FOR_LOGIN["password"],
            "name": "Karry"
        }
        status_code, response_data = user_methods.register_user(already_registered_user)
        assert status_code == 403 and response_data.get("message") == "User already exists", (
            f"Ожидался код 403, но получен {status_code}: {response_data}")

    @allure.story("Создание пользователя с отсутствующим обязательным полем")
    @allure.title('Проверка корректной ошибки при попытке создания пользователя без поля почты')
    def test_login_missing_email_field(self, user_methods):
        missing_email_data = {"password": "1234567", "email": "", "name": "name"}
        status_code, response_data = user_methods.register_user(missing_email_data)
        assert status_code == 403 and response_data.get("message") == "Email, password and name are required fields", (
            f"Ожидался код 403, но получен {status_code}: {response_data}")

    @allure.story("Создание пользователя с отсутствующим обязательным полем")
    @allure.title('Проверка корректной ошибки при попытке создания пользователя без поля пароль')
    def test_login_missing_password_field(self, user_methods):
        missing_password_data = {"login": "karry_karrow@yandex.ru", "password": "", "name": "name"}
        status_code, response_data = user_methods.register_user(missing_password_data)
        assert status_code == 403 and response_data.get("message") == "Email, password and name are required fields", (
            f"Ожидался код 403, но получен {status_code}: {response_data}")

    @allure.story("Создание пользователя с отсутствующим обязательным полем")
    @allure.title('Проверка корректной ошибки при попытке создания пользователя без поля имя')
    def test_login_missing_password_field(self, user_methods):
        missing_name_data = {"login": "karry_karrow@yandex.ru", "password": "12345", "name": ""}
        status_code, response_data = user_methods.register_user(missing_name_data)
        assert status_code == 403 and response_data.get("message") == "Email, password and name are required fields", (
            f"Ожидался код 403, но получен {status_code}: {response_data}")
