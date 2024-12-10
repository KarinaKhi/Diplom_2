USER_DATA_FOR_LOGIN = {
    "email": "karry_karrow_1_111@yandex.ru",
    "password": "password123",
    "wrong_password": "123"
}

VALID_INGREDIENT_IDS = [
    "60d3b41abdacab0026a733c6",
    "61c0c5a71d1f82001bdaaa71",
    "61c0c5a71d1f82001bdaaa6d",
    "60d3b41abdacab0026a733c7",
    "60d3b41abdacab0026a733c8"
]

INVALID_INGREDIENT_HASH = "61c0c5a43271d1f82001b4444daaa6"

LOGIN_WRONG_ALL_TEST_DATA = {
    "incorrect_login": {"email": "wrong@login.com", "password": "wrongpass"},
}

USER_REGISTRATION_EMPTY_DATA = {
    "missing_email": {"password": "1234567", "email": "", "name": "name"},
    "missing_password": {"email": "karry_karrow@yandex.ru", "password": "", "name": "name"},
    "missing_name": {"email": "karry_karrow@yandex.ru", "password": "12345", "name": ""},
}

LOGIN_WRONG_SOME_TEST_DATA = {
    "missing_email": {"email": "", "password": "1111"},
    "missing_password": {"email": "karry_karrow_1_111@yandex.ru", "password": ""},
    "missing_all_data": {"email": "", "password": ""},
}

# LOGIN_WITH_WRONG_DATA_TEST_IDS = [
#     "Missing email field",
#     "Missing password field",
#     "Empty email and password",
# ]