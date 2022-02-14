"""Написать программу, где две функции -- "Игрок 1" и "Игрок 2"
играют в игру, а третья функция -- "Судья" -- следит за ходом игры
и ведёт счёт.

Правила игры:
Оба игрока кажый раунд выдают случайное целое число
в некотором диапазоне. Судья сравнивает эти числа и начисляет игрокам очки:
Если числа равны, оба игрока получают 1 очко (+1). Когда число одно из игроков
больше другого, игрок, который выдал большее число, получает 1 очко (+1),
другой игрок штрафуется на 1 очко (-1). Игра продолжается до тех пор, пока
один из игроков не наберёт 50 очков, но не более 100 раундов."""

import random

g = 0
f = 0  # счетчики
c = [0, 0]  # конечный счетчик очков
h = [0, 0]
j = 0  # тоже какой-то счетчик


def player1():
    a = random.randint(-1000, 1000)  # игрок 1


def player2():
    b = random.randint(-1000, 1000)  # игрок 2


def referee(f, g):  # судья
    if random.randint(-1000, 1000) > random.randint(-1000, 1000):  # условие, если 1 выиграет
        f = f + 1
        g = g - 1
    elif random.randint(-1000, 1000) == random.randint(-1000, 1000):  # если ничья
        f = f + 1
        g = g + 1
    else:  # если ни то ни то
        g = g + 1
        f = f - 1
    h = [f, g]
    return h


while c[1] <= 50 and c[0] <= 50 and j <= 50:  # пока хотя бы из условий не выполнится
    print(c)
    c = [c[0] + referee(f, g)[0], c[1] + referee(f, g)[1]]
    j = j + 1

"""UPDATE 1:
Режим "Читера": после 3 проигрышей увеличивается вероятность "чита".
Чит: увеличение randint range на (+1000, +1000).
Изначальная вероятность считерить: 0%. Увеличение вероятности: +5%.
После первой победы с читом чит отключается. Вероятность чита сохраняется."""
