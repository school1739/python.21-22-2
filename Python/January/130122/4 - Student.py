### Задание №4 "Student"
##
#
# все учебные месяцы
m = ["Сентябрь", "Октябрь", "Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель", "Май", "Июнь"]
ed_grant, e = 10000, 12000
summ = e
number_m = 1
print(m[0], ":", e, 'рублей')  # расходы в первый месяц
# цикл для рассчёта и выводы  расходов
for k in range(9):
   e = e * 1.03
   print(m[number_m], ":", round(e, 2), 'рублей')
   summ = summ + e
   number_m += 1
# рассчитываем и выводим результат
print('Студенту надо попросить: ', (summ - ed_grant * 10) // 1 + 1, 'рублей')
