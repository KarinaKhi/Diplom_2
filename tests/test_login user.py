from conftest import *
import allure

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
        incorrect_data = {"email": "wrong@login.com", "password": "wrongpass"}
        status_code, response_data = user_methods.login_user(incorrect_data)
        assert (status_code == 401 and response_data["success"] is False and response_data.get(
            "message") == "email or password are incorrect"), \
            f"Получили статус {status_code} и ответ: {response_data}"

    @allure.title('Проверка корректной ошибки при попытки авторизации без поля почты')
    def test_login_missing_login_field(self, user_methods):
        missing_login_data = {"password": "1111", "email": ""}
        status_code, response_data = user_methods.login_user(missing_login_data)
        assert (status_code == 401 and response_data["success"] is False and response_data.get(
            "message") == "email or password are incorrect"), \
            f"Получили статус {status_code} и ответ: {response_data}"

    @allure.title('Проверка корректной ошибки при попытки авторизации без поля пароль')
    def test_login_missing_password_field(self, user_methods):
        missing_password_data = {"email": "karry_karrow_1_111@yandex.ru", "password": ""}
        status_code, response_data = user_methods.login_user(missing_password_data)
        print(f"1111 {response_data=}")
        assert (status_code == 401 and response_data["success"] is False and response_data.get(
            "message") == "email or password are incorrect"), \
            f"Получили статус {status_code} и ответ: {response_data}"

    @allure.title('Проверка корректной ошибки при попытке авторизации с пустыми полями')
    def test_login_missing_password_field(self, user_methods):
        missing_password_data = {"email": "", "password": ""}
        status_code, response_data = user_methods.login_user(missing_password_data)
        print(f"1111 {response_data=}")
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
