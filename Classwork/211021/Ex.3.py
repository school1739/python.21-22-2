print('Введите количество израсходованных за месяц минут разговора и смс-сообщений')
a=int(input())
b=int(input())
print('Базовая сумма тарификации: 50$')
if a>50 and b>50:
    print('Сумма за дополнительные минуты и сообщения: ' ,'%.2f' % (((a-50)*0.25)+((b-50)*0.15))+'$')
elif a<50 and b>50:
    print('Сумма за дополнительные минуты и сообщения: ' ,'%.2f' %(((b-50)*0.15))+"$")
elif a>50 and b<50:
    print("Сумма за дополнительные минуты и сообщения: " ,'%.2f' %(((a-50)*0.25))+'$')
else:
    print('Сумма за дополнительные минуты и сообщения: 0$')
print('Cумма отчислений кол-центрам 911: 0.44$')
if a>50 and b>50:
    print("Налог: " ,'%.2f' %((50+0.44+(((a-50)*0.25)+((b-50)*0.15)))*0.05)+'$')
    print("Итоговая сумма к оплате: " ,'%.2f' % ((((a-50)*0.25)+((b-50)*0.15))+((50+0.44+(((a-50)*0.25)+((b-50)*0.15)))*0.05)+50.44)+"$")
elif a<50 and b>50:
    print("Налог: ", '%.2f' % ((50 + 0.44 + ((b - 50) * 0.15)) * 0.05) + '$')
    print("Итоговая сумма к оплате: " ,'%.2f' % (((b-50)*0.15)+((50+0.44+((b-50)*0.15))*0.05)+50.44)+"$")
elif a>50 and b<50:
    print("Налог: ", '%.2f' % ((50 + 0.44 + ((a - 50) * 0.25)) * 0.05) + '$')
    print("Итоговая сумма к оплате: ", '%.2f' % (((a-50)*0.25)+((50+0.44+((a-50)*0.25))*0.05)+50.44)+"$")
else:
    print("Налог: ", '%.2f' % ((50 + 0.44) * 0.05) + '$')
    print("Итоговая сумма к оплате: ", '%.2f' % (((50 + 0.44)*0.05)+50.44)+"$")