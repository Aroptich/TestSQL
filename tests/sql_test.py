from unittest import TestCase, main

from authorization import authorization
from registration import registr
from sql import create_table, create_user, update_user, email_user, password_user, delete_user, get_id_user, list_users


class SqlTest(TestCase):


    ###########-Positive tests-###########
    def test_create_table(self):
        self.assertEqual(create_table('users'), 0)

    def test_create_user(self):
        self.assertEqual(create_user('masha@mail.ru', '12345'), 1)

    def test_update_user(self):
        self.assertEqual(update_user('aaaaaaa', 'masha@mail.ru'), 1)

    def test_email_user(self):
        self.assertEqual(email_user('masha@mail.ru'), (1, {'email': 'masha@mail.ru'}))

    def test_password_user(self):
        self.assertEqual(password_user('masha@mail.ru'),
                         (1, {'password': 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'}))

    def test_delete_user(self):
        test_user = create_user('gosha@mail.ru', '123456')
        _, data = get_id_user('gosha@mail.ru')
        self.assertEqual(delete_user(data.pop('id')), 1)

    def test_list_users(self):
        self.assertEqual(list_users(), (1, {'email': 'masha@mail.ru',
                                            'id': 1,
                                            'password': 'a7470858e79c282bc2f6adfd831b132672dfd1224c1e78cbf5bcd057'}))

    def test_authorization(self):
        self.assertEqual(authorization('masha@mail.ru', 'aaaaaaa'), None)

    def test_registr(self):
        self.assertEqual(registr('grisha@mail.ru', '123456'), None)


if __name__ == '__main__':
    main()
