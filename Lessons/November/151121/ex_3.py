import random #импортируем рандом:)
k = 0
q = ["O", "P"] #список шо бы выбирать раном символ из О(орла) и Р(решки)
l = [] #список только для последних трех монет
d = [] #список всех О и Р
for i in range(10):#цикл шо бы 10 раз выполнить то, что снизу
    while l != ["O", "O", "O"] or l != ["P", "P", "P"]:#цикл работает пока список l не равен последовательности из ООО или РРР
        ran = random.choice(q) #ну выбираем рандом монетку из спика q:)
        l.append(ran) #добавляем рандомно выбранную монетку в список
        d.append(ran) #тут тоже самое
        k += 1 #счетчик для попыток
        if len(l) > 3:
            l.pop(0) #удаляем первый элемент индекса 0 в списке из последних трех монеток:) метод нашел на форуме
        if l == ["O", "O", "O"] or l == ["P", "P", "P"]:#ну на всякий случай и чтобы добавить бреак и очистить списки

            print(d, "попыток: " + str(len(d)))#ну вывод списка из всех выпаших монет и попыток
            l.clear()#очищаем список  этот метод(clear) тоже нашел на форуме
            d.clear()#ну и еще раз тоже самое
            break
print("Среднее количество попыток: " + str(k // 10))#выводим среднее количество попыток

# Evaluation: +-OK. Надо было выводить отдельные результаты, а не списки результатов в попытке.