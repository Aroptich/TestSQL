from authorization import authorization
from registration import registr
from sql import create_table, list_users, update_user, delete_user

if __name__ == '__main__':
    #Создаем сущность в БД
    db = create_table('users')

    #Создаем нового пользователя
    new_user1 = registr('alex@mail.ru', '1234')

    # Создаем нового пользователя
    new_user2 = registr('misha@mail.ru', '12345678')

    # Создаем нового пользователя
    new_user3 = registr('oleg@mail.ru', '987654321')

    #Выводим всех пользователей в консоль
    veiws_users = list_users()

    #Изменяем пароль пользователя 'new_user1'
    update_user('11112', 'alex@mail.ru')

    #Удаляем пользователя 'new_user3'
    delete_user(3)

    # Выводим всех пользователей в консоль
    list_users()

    #Авторизация пользователя
    auth_user = authorization('misha@mail.ru', '12345678')



