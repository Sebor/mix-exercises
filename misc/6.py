# -*- coding: utf-8 -*-

"""
Имеется csv-файл вида (данные не упорядочены):

email,name
test1@mail.ru,username1
test2@gmail.com,username2
test3@gmail.com,username3
test4@rambler.ru,username4
test5@ya.ru,username5
...
testN@yahoo.com,usernameN

Используя данные из csv-файла необходимо создать список,
в котором будут содержаться группы кортежей вида (email, name) с условием,
что в каждой группе почтовые домены не должны повторяться. Пример:

[
    [
        ( ...@mail.ru, ... ),
        ( ...@gmail.com, ... ),
        ( ...@rambler.ru, ... ),
        ( ...@ya.ru, ... ),
        ( ...@..., ... ),
        ( ...@yahoo.com, ... )
    ],

    [
        ( ...@mail.ru, ... ),
        ( ...@rambler.ru, ... ),
        ( ...@ya.ru, ... ),
        ( ...@..., ... )
    ],

    ...

    [
        ( ...@mail.ru, ... ),
        ( ...@ya.ru, ... )
    ]
]

Решение должно быть оптимальным
для использования больших объемов входных данных.
"""

import csv


def create_list(csvfile):
    with open(csvfile) as f:
        reader = csv.reader(f)
        next(reader)
        lst = list(reader)
    return lst


def create_dict(csvfile):
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        for row in reader:
            #print row['email'].split('@'), row['name']
            print row


def main():
    csvfile = '6.csv'
    domain_list = []
    L = create_list(csvfile)
    for i in L:
        domain = i[0].split('@')
        if domain[1] not in domain_list:
            domain_list.append(domain[1])
    print domain_list


if __name__ == '__main__':
    main()
