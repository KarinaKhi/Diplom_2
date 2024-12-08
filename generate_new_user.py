import random
import string


def generate_new_user_and_return_login_password_name():
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    login_pass = []
    name = generate_random_string(6)
    password = generate_random_string(6)
    email = generate_random_string(6) + "@yandex.com"

    payload = {
        "name": name,
        "password": password,
        "email": email
    }
    return payload


