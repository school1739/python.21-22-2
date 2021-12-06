##
# Программа для отображения стандартной таблицы умножения от единицы до десяти
#
# Задаём переменные для диапазона границ таблицы
min_num = 1
max_num = 10
# Создаём отступ с помощью символа табуляции
print('', end="\t")
# Выводим заголовок таблицы над первой строкой
for i in range(min_num, max_num + 1):
    print(i, end="\t")
# Перевод на следующую строку
print()
# Выводим таблицу умножения
# Сначала выводим заголовок слева - один множитель для строки таблицы
for i in range(min_num, max_num + 1):
    print(i, end="\t")
    # Выводим значения столбцов перемножая значения заголовков слева и сверху
    for j in range(min_num, max_num + 1):
        print(j * i, end="\t")
    print()
