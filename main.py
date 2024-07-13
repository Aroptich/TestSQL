import hashlib

from decorators import *


@connect
@logger
def create_table(table_name) -> tuple:
    """Функция создает таблицу 'users' и возвращает строку """
    query = ("CREATE TABLE IF NOT EXISTS `%s`"
             "(`id` int(11) NOT NULL AUTO_INCREMENT,"
             "`email` varchar(100) UNIQUE NOT NULL ,"
             "`password` varchar(255) NOT NULL,"
             "PRIMARY KEY (`id`));")
    return query, table_name


@reading_data
@logger
def list_users() -> str:
    """Функуия возвращает всех пользователей из таблицы 'users'"""
    query = "SELECT * FROM `'users'`;"
    return query


@connect
@logger
def create_user(email: str, password: str) -> tuple:
    """Функция возвращает sql-запрос на создание нового пользователя в таблице `users"""
    query = ("INSERT INTO `'users'` (`email`, `password`) "
             "VALUES (%s, %s);")
    # Хеширование пароля
    hash_pass = hashlib.sha224(password.encode())
    # Преобразуем объект хеширования в шестнадцатиричное число
    safty_pass = hash_pass.hexdigest()
    return query, email, safty_pass


@connect
@logger
def update_user(new_password: str, email: str) -> tuple:
    """Функция возращает sql-запрос и новый пароль пользователя в таблице `users`"""
    query = "UPDATE `'users'` SET `password`=%s WHERE `email`=%s;"
    return query, new_password, email

@reading_data
@logger
def detial_user(email: str) -> tuple:
    """Функция проверяет по email существует ли данный пользователь в БД.
    Возвращает кортеж из sql-запроса и email"""
    query = "SELECT `email` FROM `'users'` WHERE email=%s"
    return query, email


@connect
@logger
def delete_user(id: int) -> tuple:
    """Функция возвращает sl-запрос и 'id' пользователя на удаление его из `users`"""
    query = "DELETE FROM `'users'` WHERE `id`=%s"
    return query, id

def authorization(email: str, passwor: str):
    """Функция проверяет пользователя по email"""
    pass


if __name__ == '__main__':
    # create_table('users')
    # create_user('masha@mail.ru', 'aaaaaaa')
    # create_user('dasha@mail.ru', 'bbbbbbb')
    list_users()
    # update_user('11112', 'gosha@mail.ru')
    # delete_user(1)
    detial_user('masha@mail.ru')
