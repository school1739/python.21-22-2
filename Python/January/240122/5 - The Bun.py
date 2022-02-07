"""В русской народной сказке "Колобок" песенка Колобка повторяется при каждой
встрече с очередным животным после слов "Колобок-колобок, я тебя съем!". При каждом повторении
упоминаются все предыдущие существа, от которых Колобок уже "ушёл", и добавляется новое, от которого
он только собирается сбежать.

Напишите функцию bunSong, которая получает на вход имя существа, подставляет его в песенку,
и выводит на экран. Список существ задаётся заранее вне функции. Программа итерируется по списку,
и прогоняет его через функцию для вывода всех куплетов песенки.

Hint:
Используйте отдельный список для хранения строк про животных, от которых уже ушёл главный герой.
Для добавления нового элемента в список используйте метод .append;

-> .append method
Добавляет указанный элемент в конец списка.
list.append(x) -> None
x -- Элемент, который требуется добавить в список.
    my_list = []
    my_list.append(1)
    my_list  # [1]
    my_list.append(3)
    my_list  # [1, 3]
"""

# функция
def bunsong(animal):
    print("Я Колобок, Колобок!")
    print("Я по коробу скребен,")
    print("По сусеку метен,")
    print("На сметане мешон,")
    print("Да в масле пряжон,")
    print("На окошке стужон;")
    print("Я от дедушки ушел,")
    print("Я от бабушки ушел,")
    for s in songs:
        print(s)
    print("И от тебя, ", animal, ", убегу!")
    songs.append("Я от ", animal, " ушел,")


songs = []
animals = ["заяцa", 'волка','медведя']
for animal in animals:  # вывод
    bunsong(animal)

# NOT OK:
# TypeError: list.append() takes exactly one argument (3 given)