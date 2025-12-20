from random import randint

class Person:
    user_name = 'Рашид'
    email = 'businessmanrussia2017@yandex.ru'
    password = 'Rashid123'
    
class RandomGenerate:
    user_name = 'test'
    email = f'test_user{randint(0, 9999)}@ya.ru'
    password = f'{randint(1000, 9999)}Qwe'