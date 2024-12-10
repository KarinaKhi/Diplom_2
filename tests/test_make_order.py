from conftest import *
import allure

@allure.feature("Создание заказа")
class TestCreateOrder:

    @allure.story("Создание заказа с авторизацией")
    @allure.title("Успешное создание заказа с валидными ингредиентами и авторизацией")
    def test_create_order_with_authorization_and_ingredients(self, order_methods, user_methods,
                                                             authorized_user_with_token,
                                                             random_ingredients):
        access_token = authorized_user_with_token["accessToken"]
        ingredients = random_ingredients
        status_code, response_data = order_methods.create_order(ingredients, access_token)
        assert status_code == 200 and response_data.get("success") is True, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.title("Создание заказа с авторизацией без ингредиентов")
    def test_create_order_with_authorization_without_ingredients(self, order_methods, user_methods,
                                                                 authorized_user_with_token):
        access_token = authorized_user_with_token["accessToken"]
        ingredients = []
        status_code, response_data = order_methods.create_order(ingredients, access_token)
        assert status_code == 400 and response_data.get("success") is False, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.title("Ошибка при создании заказа с неверным хешем ингредиентов с авторизацией")
    def test_create_order_with_authorization_with_invalid_ingredients_hash(self, order_methods, user_methods,
                                                                           authorized_user_with_token,
                                                                           invalid_ingredient_hash):
        access_token = authorized_user_with_token["accessToken"]
        ingredients = invalid_ingredient_hash
        status_code, response_data = order_methods.create_order(ingredients, access_token)
        assert status_code == 400 and response_data.get("success") is False, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.story("Создание заказа без авторизации")
    @allure.title("Успешное создание заказа без авторизации с ингредиентами")
    def test_create_order_without_authorization(self, order_methods, random_ingredients):
        ingredients = random_ingredients
        status_code, response_data = order_methods.create_order(ingredients)
        assert status_code == 200 and response_data.get("success") is True, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.title("Ошибка при создании заказа без авторизации и без ингредиентов")
    def test_create_order_without_ingredients(self, order_methods):
        status_code, response_data = order_methods.create_order([])
        assert status_code == 400 and response_data.get("success") is False, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")

    @allure.story("Создание заказа с неверным хешем ингредиентов")
    @allure.title("Ошибка при создании заказа с неверным хешем ингредиентов без авторизации")
    def test_create_order_with_invalid_ingredient(self, order_methods,
                                                  invalid_ingredient_hash):
        ingredients = invalid_ingredient_hash
        status_code, response_data = order_methods.create_order(ingredients)
        assert status_code == 400 and response_data.get("success") is False, (
            f"Ошибка регистрации: статус ответа {status_code}, данные ответа: {response_data}")
