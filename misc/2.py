# -*- coding: utf-8 -*-

"""
В системе авторизации есть ограничение — логин должен начинаться
с латинской буквы, он может состоять из латинских букв, цифр, точки и минуса,
но заканчиваться только латинской буквой или цифрой; минимальная длина логина
составляет 1 символ, максимальная — 20 символов. Пожалуйста, напишите код,
проверяющий соответствие входной строки этому правилу.
"""

import re

def check_login(login):
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9\.\-]{0,18}[a-zA-Z0-9]$')
    if re.match(pattern, login):
        return True
    else:
        return False


def main():
    login = '214zd65576fg-.fgk'
    result = check_login(login)
    print result


if __name__ == '__main__':
    main()