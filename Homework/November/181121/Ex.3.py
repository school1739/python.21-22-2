import random
a = 0
max = 0
i=0
while max!=100: #Ввод цикла
    b = random.randint(0, 100)
    if b> max and i!=0:#Вводд условия
        max=b
        a+=1
        print(f"{b} <== Обновление") #Вывод результата
    else:
        print(b) #Вывод результата
    i+=1
print(f"Максимальное значение в ряду: 100 "f"\nКоличество смен максимального значения: {a}") #Вывод результата

# Evaluation: OK