### Задание №1 "Hypotenuse"
##
#
# функция для расчёта гипотенузы
def hypo(k1, k2):
   t = (k1 ** 2 + k2 ** 2) ** 0.5
   print("Гипотенуза равна", t)


# запрашиваем у пользователя значения катетов
a = int(input("Введите значение первого катета: "))
b = int(input("Введите значение второго катета: "))

# вызов функции
hypo(a, b)

# OK