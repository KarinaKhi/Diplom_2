from conftest import *
import allure


@allure.story("Изменение данных пользователя")
@allure.title("Успешное изменение имени и почты с авторизацией")
def test_update_user_with_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    new_name = add_random_letter_to_string(user_data["name"])
    new_email = add_random_letter_to_string(user_data["email"])
    updated_data = {"name": new_name, "email": new_email}
    status_code, response_data = user_methods.update_user(user_data["accessToken"], updated_data)
    assert status_code == 200 and response_data["success"] is True, (
        f"Ожидался статус 200, получено {status_code}: {response_data}")


@allure.title("Успешное изменение имени с авторизацией")
def test_update_user_name_with_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    new_name = add_random_letter_to_string(user_data["name"])
    email = user_data["email"]
    updated_data = {"name": new_name, "email": email}
    status_code, response_data = user_methods.update_user(user_data["accessToken"], updated_data)
    assert status_code == 200 and response_data["success"] is True, (
        f"Ожидался статус 200, получено {status_code}: {response_data}")


@allure.title("Успешное изменение имени и почты с авторизацией")
def test_update_user_email_with_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    name = user_data["name"]
    new_email = add_random_letter_to_string(user_data["email"])
    updated_data = {"name": name, "email": new_email}
    status_code, response_data = user_methods.update_user(user_data["accessToken"], updated_data)
    assert status_code == 200 and response_data["success"] is True, (
        f"Ожидался статус 200, получено {status_code}: {response_data}")


@allure.title("Ошибка изменения имени и почты без авторизации")
def test_update_user_without_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    new_name = add_random_letter_to_string(user_data["name"])
    new_email = add_random_letter_to_string(user_data["email"])
    updated_data = {"name": new_name, "email": new_email}
    status_code, response_data = user_methods.update_user(None, updated_data)
    assert status_code == 401 and response_data["success"] is False and response_data.get(
        "message") == "You should be authorised", \
        f"Ожидался статус 401, получено {status_code}: {response_data}"


@allure.title("Ошибка изменения имени  без авторизации")
def test_update_user_without_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    new_name = add_random_letter_to_string(user_data["name"])
    email = user_data["email"]
    updated_data = {"name": new_name, "email": email}
    status_code, response_data = user_methods.update_user(None, updated_data)
    assert status_code == 401 and response_data["success"] is False and response_data.get(
        "message") == "You should be authorised", \
        f"Ожидался статус 401, получено {status_code}: {response_data}"


@allure.title("Ошибка изменения почты без авторизации")
def test_update_user_without_authorization(user_methods, authorized_user_with_token):
    user_data = authorized_user_with_token
    name = user_data["name"]
    new_email = add_random_letter_to_string(user_data["email"])
    updated_data = {"name": name, "email": new_email}
    status_code, response_data = user_methods.update_user(None, updated_data)
    assert status_code == 401 and response_data["success"] is False and response_data.get(
        "message") == "You should be authorised", \
        f"Ожидался статус 401, получено {status_code}: {response_data}"
