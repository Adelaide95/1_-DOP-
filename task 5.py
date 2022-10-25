#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Определить значение функции Z=1/(XY) при X и Y не равных 0.
Выполнила: Хацукова Аделаида.
"""
if __name__ == '__main__':
    x = float(input("Введите x: "))
    y = float(input("Введите y: "))
    if x and y != 0:
        print(f"Значение функции Z = 1/(x*y)= {1 / (x * y)}")
    else:
        print("А ну убрал быстро ноль из переменных!")
