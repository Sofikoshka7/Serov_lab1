import random
import matplotlib
from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as mpl

matplotlib.use('TkAgg')


n = 13
num = 20
a = int(input('1 - Задать точки случайно, 2 - Показать решение по тетради\n'))
if a == 1:
    num = int(input("Введите количество точек\n"))
k1 = 1
k2 = 0.85
k3 = 0.75
count = 0
lst = []


class Point:
    def __init__(self, x, y, status='V', wasactive="-", dele='', bi=0, bname='', findex=0, fstatus=0):
        self.x = x
        self.y = y
        self.status = status
        self.wasactive = wasactive
        self.dele = dele
        self.bi = bi
        self.bname = bname
        self.findex = findex
        self.fstatus = fstatus


while count < num:
    if a == 1:
        y = random.uniform(3.81, 26)
        x = random.uniform(6.5, 26)
        if (y <= n + x) and (y >= 2 * n - x) and ((x - n) ** 2 + (y - n) ** 2 <= n ** 2):
            lst.append(Point(x, y))
            count = count + 1
    else:
        lst.append(Point(8, 20))
        lst.append(Point(10, 21))
        lst.append(Point(10, 18))
        lst.append(Point(26, 13))
        lst.append(Point(21, 8))
        lst.append(Point(15, 13))
        lst.append(Point(15, 19))
        lst.append(Point(13, 16))
        lst.append(Point(20, 11))
        lst.append(Point(18, 15))
        lst.append(Point(14, 23))
        lst.append(Point(23, 8))
        lst.append(Point(24, 12))
        lst.append(Point(22, 14))
        lst.append(Point(21, 18))
        lst.append(Point(18, 21))
        lst.append(Point(13, 20))
        lst.append(Point(16, 22))
        lst.append(Point(16, 16))
        lst.append(Point(19, 19))
        count = num


test_number = 0
while True:
    test_text = input("Выберите, что вывести:\n0 - График с точками\n1 - Множество Парето на графике\n2 - Кластеры с раскраской по эффективности\n")
    test_number = int(test_text)
    if test_number == 0:
        y1 = lambda x: n + x
        y2 = lambda x: (n * 2) - x
        fig, axes = mpl.subplots()
        x = np.linspace(0, 40, 2)
        drawing_uncolored_circle = mpl.Circle((n, n), n, color='c', fill=False,
                                              label='(f1 - 13)^2 + (f2 - 13)^2 <= 169')
        axes.set_aspect(1)
        axes.add_artist(drawing_uncolored_circle)
        mpl.plot(x, y1(x), color='b', label='-f1 + f2 <= 13')
        mpl.plot(x, y2(x), color='r', label='f1 + f2 >= 26')
        for i in range(num):
            mpl.plot(lst[i].x, lst[i].y, marker=".", color="k")
        mpl.xlabel("F1")
        mpl.ylabel("F2")
        mpl.legend(fontsize='xx-small', frameon=False)
        mpl.suptitle('График')
        mpl.savefig('Figure.png')
        mpl.show()
    elif test_number == 1:
        for i in range(num):
            for j in range(num):
                if (lst[i].status == 'V') and (i != j):
                    lst[i].wasactive = '+'
                    if (lst[j].x <= lst[i].x) and (lst[j].y <= lst[i].y) and (lst[j].status != 'X'):
                        lst[j].status = 'X'
                        j1 = j + 1
                        lst[i].dele = lst[i].dele + str(j1) + ' '

        pt1 = PrettyTable()
        pt1.field_names = ["id", "f1", "f2", 'V/X', 'Use', 'Del']
        for i in range(num):
            pt1.add_row([i + 1, lst[i].x, lst[i].y, lst[i].status, lst[i].wasactive, lst[i].dele])
        print(pt1)

        y1 = lambda x: n + x
        y2 = lambda x: (n * 2) - x
        fig, axes = mpl.subplots()
        x = np.linspace(0, 40, 2)
        drawing_uncolored_circle = mpl.Circle((n, n), n, color='c', fill=False,
                                              label='(f1 - 13)^2 + (f2 - 13)^2 <= 169')
        axes.set_aspect(1)
        axes.add_artist(drawing_uncolored_circle)
        mpl.plot(x, y1(x), color='b', label='-f1 + f2 <= 13')
        mpl.plot(x, y2(x), color='r', label='f1 + f2 >= 26')
        for i in range(num):
            if lst[i].status == 'V':
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="k")
        mpl.xlabel("F1")
        mpl.ylabel("F2")
        mpl.suptitle('Множество Парето')
        mpl.savefig('Figure2.png')
        mpl.show()
    elif test_number == 2:
        y1 = lambda x: n + x
        y2 = lambda x: (n * 2) - x
        fig, axes = mpl.subplots()
        x = np.linspace(0, 40, 2)
        drawing_uncolored_circle = mpl.Circle((n, n), n, color='c', fill=False, label='(f1 - 20)^2 + (f2-20)^2 <= 169')
        axes.set_aspect(1)
        axes.add_artist(drawing_uncolored_circle)
        mpl.plot(x, y1(x), color='b', label='-f1 + f2 <= 13')
        mpl.plot(x, y2(x), color='r', label='f1 + f2 >= 26')
        for i in range(num):
            for j in range(num):
                if i != j:
                    if (lst[j].x >= lst[i].x) and (lst[j].y >= lst[i].y):
                        lst[i].bi = lst[i].bi + 1
                        j1 = j + 1
                        lst[i].bname = lst[i].bname + str(j1) + ' '
            lst[i].findex = 1 / (1 + (lst[i].bi / (num - 1)))
            if (abs(k1 - lst[i].findex) < abs(k2 - lst[i].findex)) and (
                    abs(k1 - lst[i].findex) < abs(k3 - lst[i].findex)):
                lst[i].fstatus = 1
            elif (abs(k2 - lst[i].findex) < abs(k1 - lst[i].findex)) and (
                    abs(k2 - lst[i].findex) < abs(k3 - lst[i].findex)):
                lst[i].fstatus = 2
            elif (abs(k3 - lst[i].findex) < abs(k1 - lst[i].findex)) and (
                    abs(k3 - lst[i].findex) < abs(k2 - lst[i].findex)):
                lst[i].fstatus = 3
        pt2 = PrettyTable()
        pt2.field_names = ["id", "f1", "f2", "bi", 'bi()', 'Ф', 'Ki']
        for i in range(num):
            pt2.add_row([i + 1, lst[i].x, lst[i].y, lst[i].bi, lst[i].bname, lst[i].findex, lst[i].fstatus])
        print(pt2)

        # Вывод кластеров по индексам эффективности
        count1 = 0
        count2 = 0
        count3 = 0
        for i in range(num):
            if lst[i].fstatus == 1 and (count1 == 0):
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="g")
                count1 = count1 + 1
        for i in range(num):
            if lst[i].fstatus == 2 and (count2 == 0):
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="y")
                count2 = count2 + 1
        for i in range(num):
            if lst[i].fstatus == 3 and (count3 == 0):
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="m")
                count3 = count3 + 1
        for i in range(num):
            if lst[i].fstatus == 1:
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="g")
            if lst[i].fstatus == 2:
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="y")
            if lst[i].fstatus == 3:
                mpl.plot(lst[i].x, lst[i].y, marker=".", color="m")
        mpl.suptitle('Кластеры')
        mpl.xlabel("F1")
        mpl.ylabel("F2")
        mpl.legend(['1', '2', '3'], fontsize='xx-small')
        mpl.savefig('Figure3.png')
        mpl.show()
