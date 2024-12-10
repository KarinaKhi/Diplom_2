from conftest import *
import allure
from data import *


@allure.feature("Логин пользователя")
class TestLoginUser:

    @allure.story("Успешный логин под существующим пользователем")
    def test_login_existing_user(self, user_methods, user_data_login):
        status_code, response_data = user_methods.login_user(user_data_login)
        assert (status_code == 200 and response_data["success"] is True and "accessToken" in response_data), \
            f"Получили статус {status_code} и сообщение '{response_data.get('message', 'Нет сообщения')}'"

    @allure.story("Логин с неверным логином и паролем")
    @allure.title('Проверка корректной ошибки при попытке авторизации с некорректными данными в обоих полях')
    def test_login_with_incorrect_data(self, user_methods):
        incorrect_data = LOGIN_WRONG_ALL_TEST_DATA["incorrect_login"]
        status_code, response_data = user_methods.login_user(incorrect_data)
        assert response_data.get("message") == "email or password are incorrect", \
            f"Ожидали сообщение 'email or password are incorrect', получили: {response_data.get('message')}"

    @pytest.mark.parametrize(
        "test_data",
        [
            (LOGIN_WRONG_SOME_TEST_DATA["missing_email"]),
            (LOGIN_WRONG_SOME_TEST_DATA["missing_password"]),
            (LOGIN_WRONG_SOME_TEST_DATA["missing_all_data"]),
        ],
        ids=[
            "Missing email field",
            "Missing password field",
            "Missing all fields"
        ]
    )
    @allure.title("Проверка корректной ошибки при некорректной авторизации: {test_data_key}")
    def test_login_error_handling(self, user_methods, test_data):
        status_code, response_data = user_methods.login_user(test_data)
        assert (status_code == 401 and response_data["success"] is False and response_data.get(
            "message") == "email or password are incorrect"), \
            f"Получили статус {status_code} и ответ: {response_data}"

    @allure.title('Проверка корректной ошибки при попытки авторизации с некорректным паролем')
    def test_login_with_incorrect_password(self, user_methods, user_data_login):
        correct_login = user_data_login["email"]
        incorrect_password_data = {"email": correct_login, "password": "wrongpass12345"}
        status_code, response_data = user_methods.login_user(incorrect_password_data)
        assert (status_code == 401 and response_data["success"] is False and response_data.get(
            "message") == "email or password are incorrect"), \
            f"Получили статус {status_code} и ответ: {response_data}"
