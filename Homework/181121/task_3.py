##
# Смена лидера
#
# Импортируем модуль random
import random

# Задаём переменную количества смен максимального значения
updates = 0
# Генерируем случайное первое число в ряду и задаём его как максимум
max_num = random.randint(1, 100)
# Выводим его значение
print(max_num)
# Задаём цикл для следующих 99 случайных чисел
for i in range(1, 100):
    # Генерируем целое случайное число от 1 до 100
    num = random.randint(1, 100)
    # Если число больше максимального
    if num > max_num:
        # Присваиваем переменной новый максимум
        max_num = num
        updates += 1
        print(f"{num} <== Обновление максимума")
    else:
        # Иначе просто выводим число
        print(num)
# Выводим оповещение для пользователя
print("Максимальное значение в ряду:", max_num)
print("Количество смен максимального значения:", updates)

# Evaluation: OK