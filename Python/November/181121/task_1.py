##
# Перевод из десятичной СС в двоичную "столбиком"
#
# Запрашиваем целое число у пользователя
n = int(input("Введите целое число: "))
# Присваиваем переменной result значение пустой строки
result = ''
# Задаём цикл пока целое число после деления на 2 не станет равно нулю
while n != 0:
    remainder = n % 2
    integer = n // 2
    print(
        f"Целая часть от деления: {integer}, Остаток: {remainder}"
    )
    # Преобразовываем значение остатка в строку
    # и добавляем ее в начало переменной result
    result = str(remainder) + result
    # Присваиваем новое значение переменной для деления числа из целой части
    n = integer
# Выводим результат
print("Результат:", result)

# Evaluation: OK