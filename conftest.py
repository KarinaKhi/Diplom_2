import allure
import pytest
from generate_new_user import generate_new_user_and_return_login_password_name
from methods.user_methods import *
import random
import string
from data import VALID_INGREDIENT_IDS, INVALID_INGREDIENT_HASH
from methods.order_methods import *


@allure.step("Инициализация методов работы с пользователем")
@pytest.fixture()
def user_methods():
    return UserMethods()


@pytest.fixture()
def random_user_data():
    return generate_new_user_and_return_login_password_name()


@pytest.fixture()
def user_data_login():
    user_methods = UserMethods()
    data = generate_new_user_and_return_login_password_name()
    response = requests.post(f"{BASE_URL}/api/auth/register", json=data)
    login_pass = []
    access_token = None
    if response.status_code == 200:
        login_pass.append(data["email"])
        login_pass.append(data["password"])
        login_pass.append(data["name"])
        access_token = response.json().get("accessToken")
    print(f"status_code={response.json} {login_pass=}", flush=True)
    yield {"email": login_pass[0], "password": login_pass[1], "name": login_pass[2]}
    user_methods.delete_user(access_token)


@pytest.fixture()
def authorized_user_with_token(user_methods):
    user_data = generate_new_user_and_return_login_password_name()
    status_code, response = user_methods.register_user(user_data)
    access_token = response.get("accessToken")
    yield {
        "accessToken": access_token,
        "email": user_data["email"],
        "name": user_data["name"],
        "password": user_data["password"]
    }
    user_methods.delete_user(access_token)


def add_random_letter_to_string(original_string):
    random_letter = random.choice(string.ascii_letters)
    return random_letter + original_string


@allure.step("Инициализация методов работы с заказами")
@pytest.fixture()
def order_methods():
    return OrderMethods()


@pytest.fixture
def random_ingredients():
    return VALID_INGREDIENT_IDS[:3]


@pytest.fixture
def invalid_ingredient_hash():
    return INVALID_INGREDIENT_HASH[:0]
