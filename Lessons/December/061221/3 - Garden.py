# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза')

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка')

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)

# выведите на консоль все виды цветов
a_set=garden_set | meadow_set
print("Все цветы:")
for i in a_set:
    print(i)
print("")

# выведите на консоль те, которые растут и там и там
a_set=garden_set & meadow_set
print("и там и там:")
for i in a_set:
    print(i)
print("")

# выведите на консоль те, которые растут в саду, но не растут на лугу
b_set=garden_set-a_set
print("которые только в саду:")
for i in b_set:
    print(i)
print("")

# выведите на консоль те, которые растут на лугу, но не растут в саду
print("которые только на лугу:")
a_set=meadow_set-a_set
for i in a_set:
    print(i)
print("")

# Evaluation: OK