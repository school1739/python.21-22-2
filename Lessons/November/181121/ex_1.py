n = int(input())#обычный воод от пользователя
result = ''#пустая строка
while n > 0:#цикл
    result = str(n % 2) + result#записываем в строку, точнее конкантенируем выделение остатка и предыдущий символ (0/1)
    n = n // 2
print(result)#отвеет:)

# Evaluation: OK