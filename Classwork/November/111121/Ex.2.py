cen = str(input())
k = 0
while cen != "": #начало цикла
    k = k + int(cen)
    cen = str(input())
    if cen =="": #введение команды Enter для завершения цикла
        break
print((k + (-k % 5))) #завершение цикла

# Evaluation: OK