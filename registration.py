from sql import create_user


def registr(email: str, password: str):
    """Функция позволяет регестрировать пользователя и записывать его данные в БД"""
    if create_user(email, password) is None:
        raise ValueError(f'Пользователь с таким {email} уже существует!')
    print(f'Пользователь успешно зарегестрирован')