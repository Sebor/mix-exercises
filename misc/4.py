# -*- coding: utf-8 -*-

"""
Имеется лог веб-сервера, где каждая строка соответствует
одному обращению клиента к веб-серверу. Формат лога:

...
127.0.0.1 - frank [10/Oct/2000:13:55:36 -0700] "GET /index.php HTTP/1.0" 200 2326
...

Найти пять IP-адресов, от которых было больше всего запросов.
"""

from collections import Counter


def count_ip(logfile):
    addresses = []
    with open(logfile) as f:
        for line in f:
            line = line.split()
            addresses.append(line[0])
    for ip in Counter(addresses).most_common(5):
        print ip[0]


def main():
    logfile = 'log.log'
    count_ip(logfile)


if __name__ == '__main__':
    main()
