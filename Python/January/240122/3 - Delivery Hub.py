### Задание №3 "Delivery Hub"
##
#
# функия для расчёта суммы покупки
def sum(count):
   summa = (10.95 + (count - 1) * 2.95) * 75  # делаем вычисления
   print("Итого к оплате: " + str(round(summa, 4)) + "₽")  # выводим результат


# запрашиваем у пользователя количество покупок
colichestvo = int(input("Введите количество товаров: "))

# вызов функции
sum(colichestvo)

# OK