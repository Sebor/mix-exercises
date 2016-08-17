# -*- coding: utf-8 -*-

"""
Есть два списка разной длины.
В первом содержатся ключи, а во втором значения.
Напишите функцию, которая создаёт из этих ключей и значений словарь.
Если ключу не хватило значения, в словаре должно быть значение None.
Значения, которым не хватило ключей, нужно игнорировать.
"""


def lists_dic(list_key, list_value):
    if len(list_key) > len(list_value):
        values = map(None, list_key, list_value)
    else:
        values = zip(list_key, list_value)
    return dict(values)


def main():
    list_key = [x for x in range(1, 5)]
    list_value = [x for x in range(1, 8)]
    print lists_dic(list_key, list_value)


if __name__ == '__main__':
    main()