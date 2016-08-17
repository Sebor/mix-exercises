# -*- coding: utf-8 -*-

"""
Имеются 2 таблицы — users и messages:

users [ uid, name ]
messages [ uid, msg ]

Используя sqlite3 создайте базу данных и соответствующие таблицы
(напишите SQL для создания таблиц). Напиши SQL-запрос,
результатом которого будет выборка из двух полей:
«Имя пользователя» и «Общее количество сообщений».
"""

import sqlite3 as sql


def create_db(dbfile):
    con = sql.connect(dbfile)
    with con:
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS '
                    'users(uid INTEGER PRIMARY KEY, name TEXT)')
        cur.execute('CREATE TABLE IF NOT EXISTS '
                    'messages(uid INTERGER,'
                    'msg TEXT, FOREIGN KEY(uid) REFERENCES users(uid))')


def make_req(dbfile):
    con = sql.connect(dbfile)
    with con:
        cur = con.cursor()
        cur.execute('SELECT name, count(*) FROM users JOIN messages '
                    'ON users.uid = messages.uid GROUP BY users.uid')
        for row in cur.fetchall():
            print row


def main():
    dbfile = 'dbfile.sqlite'
    create_db(dbfile)
    make_req(dbfile)


if __name__ == '__main__':
    main()