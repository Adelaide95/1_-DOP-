#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Известен объем информации в байтах. Перевести в килобайты, мегабайты.
Выполнила: Хацукова Аделаида.
"""
if __name__ == '__main__':
    bytes = int(input("Введите вес в байтах: "))
    print(f"Объем в килобайтах: {bytes/1024}\n"f"Объем в мегабайтах: {bytes/(1024*1024)}")
