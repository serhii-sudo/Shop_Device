from django.test import TestCase


class TestMainPage(TestCase):
    def test_url_exists_at_correct_location(self):
        response = self.client.get('')  # тестирование на ответ статус кода 200
        self.assertEqual(response.status_code, 200)

    def test_template_name_correct(self):
        response = self.client.get('')  # тестирование шаблонов html
        self.assertTemplateUsed(response, 'store/home.html')

    def test_template_content(self):
        response = self.client.get('')
        self.assertContains(response, '<h1>Home Page</h1>', html=True)


#  ://forum.djangoproject.com/t/django-tests-dont-use-test-database-if-alias-is-not-specified-in-testcases/15331/2

# python manage.py test --keepdb, при запусках тестов не забываем данный флаг, если не хотим чтобы Джанго удалял
# тестовую базу данных(Preserving test database for alias 'default'..)
# (django destroying test database for alias 'default'), чтобы удалять тестовую бд - команда без флага!!


# TЕСТЫ ЗАПУСКАЮТСЯ НА ОТКЛЮЧЕННОМ СЕРВЕРЕ!!!!!

'''Вообще говоря, (SimpleTestCase) используется, когда база данных не нужна,
в то время как (TestCase) используется,
когда вы хотите протестировать базу данных или у вас уже просто есть бд.
(TransactionTestCase) полезно тестировать транзакции базы данных напрямую,
пока (LiveServerTestCase) запускает поток сервера для тестирования с помощью браузерных инструментов,
таких как Selenium. '''
