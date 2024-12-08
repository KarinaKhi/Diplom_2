from conftest import *
import allure

@allure.feature("Orders")
class TestGetOrders:

    @allure.title("Успешное получение заказов при наличии заказа у авторизованного пользователя")
    def test_get_orders_with_authorization(self, order_methods, authorized_user_with_token, random_ingredients):
        access_token = authorized_user_with_token["accessToken"]
        order_methods.create_order(random_ingredients, access_token)
        status_code, response_data = order_methods.get_orders(access_token)
        assert status_code == 200 and response_data["success"] is True and len(response_data.get("orders")) > 0, (
            f"Ожидался статус 200, получено {status_code}: {response_data}")

    @allure.title("Успешное получение заказов при отсутствии заказа у авторизованного пользователя")
    def test_get_orders_with_authorization_without_any_order(self, order_methods, authorized_user_with_token,
                                                             random_ingredients):
        access_token = authorized_user_with_token["accessToken"]
        status_code, response_data = order_methods.get_orders(access_token)
        assert status_code == 200 and response_data["success"] is True and len(response_data.get("orders")) == 0, (
            f"Ожидался статус 200, получено {status_code}: {response_data}")

    @allure.title("Ошибка при получении заказов неавторизованным пользователем")
    def test_get_orders_without_authorization(self, order_methods, random_ingredients):
        order_methods.create_order(random_ingredients)
        status_code, response_data = order_methods.get_orders()
        assert status_code == 401 and response_data["success"] is False and response_data[
            "message"] == "You should be authorised", \
            f"Ожидался статус 401, получено {status_code}: {response_data}"
