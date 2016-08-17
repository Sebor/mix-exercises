# -*- coding: utf-8 -*-

"""
По адресу http://www.cbr.ru/scripts/XML_daily.asp находятся данные
о курсе валют. Необходимо получить данные по соответствующему url
и извлечь курс доллара и евро по отношению к рублю.
"""

import urllib2
import xml.etree.ElementTree as ET


def exchange_rates(url):
    tree = ET.ElementTree(file=urllib2.urlopen(url))
    root = tree.getroot()
    for currency in root.findall('Valute'):
        name = currency.find('Name').text
        value = currency.find('Value').text
        if name == u'Доллар США' or name == u'Евро':
            print name, value


def main():
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    exchange_rates(url)


if __name__ == '__main__':
    main()