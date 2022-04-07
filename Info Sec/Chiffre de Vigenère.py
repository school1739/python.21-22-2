# Напишите программу, шифрующую входящее сообщение с помощью шифра Виженера.
# Шифр Виженера представляет собой шифр Цезаря с переменной величиной сдвига.
# Величину сдвига задают ключевым словом.
# Например слово БАЗА означает последовательность сдвигов исходных букв: 219121912191...

alphabet_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
key_list=[]
print("Выбирите язык, указав его порядковый номер.")
print("1. Русский")
print("2. Английский")
n = input("Введите номер: ")
if n =="1":
    key_text = str.upper(input("KEY: "))
    plain_text = str.upper(input("PLAIN: "))
    
    for key in key_text:
        key_list+=key
    if len(key_text)<len(plain_text):
        for _ in range((len(plain_text)-len(key_text))//2+1):
            key_list+=key_list
    for i in range (len(plain_text)):
        plain_index = alphabet_RU.find(plain_text[i])
        key_index = alphabet_RU.find(key_list[i])+1
        print(alphabet_RU[plain_index+key_index])
else:
    key_text = input("KEY: ")
    plain_text = input("PLAIN: ")


    for key in key_text:
        key_list+=key
    if len(key_text) < len(plain_text):
        for _ in range(len(plain_text) - len(key_text)):
            key_list += key_list
    for i in range(len(plain_text)):
        plain_index = alphabet_EU.find(plain_text[i])
        key_index = alphabet_EU.find(key_list[i])+1
        print(alphabet_EU[plain_index+key_index])