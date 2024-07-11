from datetime import datetime

import pymysql

from config import host, port, password, user, db_name


def connect(func):
    """Функция-декоратор для связи с БД"""

    def wrapper(*args, **kwargs):
        try:
            connection = pymysql.connect(
                host=host,
                port=port,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Соединение с БД установлено")
            try:
                with connection.cursor() as cursor:
                    if isinstance(func(*args, **kwargs), tuple):
                        sql, *values = func(*args, **kwargs)
                        if values is not None:
                            cursor.execute(sql, values)
                        else:
                            cursor.execute(sql)
                    else:
                        cursor.execute(func(*args, **kwargs))
                    connection.commit()
            finally:
                connection.close()

        except Exception as err:
            print("В соединение с БД отказано...")
            print(err)

    return wrapper


def logger(func):
    """Функция-декоратор для логирования команд БД"""

    def wrapper(*args, **kwargs):
        try:
            with open('log.txt', 'a', encoding='utf-8') as file:
                query = func(*args, **kwargs)
                file.writelines(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
                file.writelines(f"{'=' * 35}\n")
                file.writelines(f'{query}\n')
                file.writelines(f"{'=' * 35}\n")
                return query
        except Exception as err:
            print(err)

    return wrapper


@connect
@logger
def create_table(table_name) -> tuple:
    """Функция создает таблицу 'users' и возвращает строку """
    query = ("CREATE TABLE IF NOT EXISTS `%s`"
            "(`id` int(11) NOT NULL AUTO_INCREMENT,"
            "`email` varchar(100) NOT NULL," 
            "`password` varchar(255) NOT NULL,"
            "PRIMARY KEY (`id`))")
    return query, table_name


@connect
@logger
def list_users() -> str:
    """Функуия возвращает всех пользователей из таблицы 'users'"""
    query = "SELECT * FROM `'users'`"
    return query


@connect
@logger
def create_user(email: str, password: str) -> tuple:
    """Функция возвращает sql-запрос на создание нового пользователя"""
    query = ("INSERT INTO `'users'` (`email`, `password`) "
            "VALUES (%s, %s)")
    return query, email, password


if __name__ == '__main__':
    create_table('users')
    create_user('gosha@mail.ru', '123456')
    # list_users()
