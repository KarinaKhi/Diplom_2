from conftest import *
import allure
from data import *


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

    @pytest.mark.parametrize(
        "test_data",
        [
            (USER_REGISTRATION_EMPTY_DATA["missing_email"]),
            (USER_REGISTRATION_EMPTY_DATA["missing_password"]),
            (USER_REGISTRATION_EMPTY_DATA["missing_name"]),
        ],
        ids=[
            "Missing email field",
            "Missing password field",
            "Missing name field"
        ]
    )
    @allure.story("Создание пользователя с отсутствующим обязательным полем")
    @allure.title('Проверка корректной ошибки при попытке создания пользователя с отсутствующим обязательным полем')
    def test_user_creation_with_missing_fields(self, user_methods, test_data):
        status_code, response_data = user_methods.register_user(test_data)
        assert status_code == 403 and response_data.get("message") == "Email, password and name are required fields", (
            f"Ожидался код 403, но получен {status_code}: {response_data}")
