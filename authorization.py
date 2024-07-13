import hashlib

from sql import email_user, password_user


def authorization(email: str, password: str):
    """Функция проверяет пользователя по email"""
    if email_user(email) is None:
        raise ValueError(f'Пользователя с таким {email} нет в БД')
    # Хеширование пароля
    auth_pass = hashlib.sha224(password.encode())
    # Преобразуем объект хеширования в шест
    auth_pass = auth_pass.hexdigest()
    #Данные пользователя(id,data)
    id, data = password_user(email)
    #Захешированный пароль пользователя из БД
    safty_pass = data.pop('password')
    if auth_pass != safty_pass:
        raise ValueError(f'Неверный пароль')
    print(f'Авторизация прошла успешно!')