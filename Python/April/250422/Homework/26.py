"""Предприятие производит закупку изделий A и B, на которую выделена определённая сумма денег.
У поставщика есть в наличии различные модификации этих изделий по различной цене.
При покупке необходимо руководствоваться следующими правилами:

1. Нужно купить как можно больше изделий, независимо от их типа и модификации.
2. Если можно разными способами купить максимальное количество изделий, нужно выбрать тот способ,
    при котором будет куплено как можно больше изделий B.
3. Если можно разными способами купить максимальное количество изделий с одинаковым количеством изделий B,
    нужно выбрать тот способ, при котором вся покупка будет дешевле.

Определите, сколько всего будет куплено изделий B и какая сумма останется неиспользованной.

Входные данные.

Первая строка входного файла содержит два целых числа: N — общее количество изделий у поставщика и M — сумма
выделенных на закупку денег (в рублях). Каждая из следующих N строк содержит целое число (цена изделия в рублях)
и символ (латинская буква A или B), определяющий тип изделия. Все данные в строках входного файла отделены одним пробелом.
В ответе запишите два целых числа: сначала количество закупленных изделий типа B, затем оставшуюся неиспользованной сумму денег.
Пример входного файла:

6 130
30 A
50 A
60 B
20 B
70 B
10 A

В данном случае можно купить не более 4 изделий, из них не более 2 изделий B.
Минимальная цена такой покупки 120 рублей (покупаем изделия 30A, 60B, 20B, 10A).
Останется 10 рублей. В ответе надо записать числа 2 и 10."""

with open('26.txt', 'r') as file:  # открываем файл для чтения
    lines = file.readlines()  # читаем строки файла, записывая в переменную

    first_line = lines.pop(0).split()  # отделяем первую строчку

    goods = int(first_line[0])  # определям кол-во товаров
    money_1 = int(first_line[1])  # определяем сумму денег

    lines.sort()  # сортируем по возрастанию

    goods_count = 0  # кол-во купленных товаров
    money_2 = money_1  # те же деньги, но для первой проверки  максимального кол-ва товаров

    # кол-во товара В и Ф
    B_count = 0
    A_count = 0

    #  пока пустые списки товаров В и А
    B_goods = []
    A_goods = []

    # состаляем списки товаров В и А
    for line in lines:
        if line[5] == "B":
            B_goods.append(line[0:4])
        elif line[5] == "A":
            A_goods.append(line[0:4])

    for line in lines:
        if money_2 >= int(line[0:4]):  # проверяем сумму оставшихся денег и цену товаров
            goods_count += 1  # увеличиваем кол-во товаров
            money_2 -= int(line[0:4])  # вычитаем цену товара из суммы денег
        else:
            break

    # ищем максимальное количество товаров В, ктороые можно купить
    for good in B_goods:
        if money_1 >= int(good):  # проверяем сумму оставшихся денег и цену товаров
            B_count += 1  # увеличиваем кол-во товаров В
            money_1 -= int(good)  # вычитаем цену товара из суммы денег
        else:
            break
    # пока кол-во товаров В и А меньше общего кол-ва товаров добавляем товары А и убираем самый дорогой товар В, если деньги кончились
    while (B_count + A_count < goods_count):
        if money_1 >= int(A_goods[A_count]):
            money_1 -= int(A_goods[A_count])
            A_count += 1
        else:
            B_count -= 1
            money_1 += int(B_goods[B_count])

print(B_count, money_1)  # выводим кол-во товара В и оставшиеся деньги