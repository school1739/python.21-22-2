import math

x1 = input("Введите координату первой точки по Х: ")
y1 = input("Введите координату первой точки по У: ")
x2 = input("Введите координату второй точки по Х: ")
y2 = input("Введите координату второй точки по У: ")
P = 0
first_point_x = x1
first_point_y = y1
while x1 != "" or y2 != "" or x2 != "" or y2 != "":
    if x2 == "" or y2 == "":  # Проверка на пустую строку
        x2 = int(first_point_x)
        y2 = int(first_point_y)
        break
    length = abs(math.sqrt((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2))  # Вычисляем длину стороны фигуры
    P = P + length  # Вычисляем периметр на данной стадии
    x1 = int(x2)
    y1 = int(y2)
    x2 = input("Введите координату следующей точки по Х: ")
    y2 = input("Введите координату следующей точки по У: ")
length = math.sqrt(
    (int(first_point_x) - int(x1)) ** 2 + (int(first_point_y) - int(y1)) ** 2)  # Вычисляем длину последней стороны
P = P + length  # Вычисляем итоговый периметр
print("%.2f" % P)  # Выводим результат
