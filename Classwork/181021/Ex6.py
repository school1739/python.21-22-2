x = int(input())
if x < 40:
    print('Ниже минимального')
elif x == 40:
    print('Тихая Комната')
elif x < 70:
    print('Тихая комната - Будильник')
elif x == 70:
    print('Будильник')
elif x < 106:
    print('Будильник - Газонокосилка')
elif x == 106:
    print('Газонокосилка')
elif x < 130:
    print('Газонокосилка - Отбойный молоток')
elif x ==130:
    print('Отбойный молоток')
else:
    print('Выше максимального')

# Evaluation: OK
