import datetime
year=int(input())
month=int(input())
day=int(input())
tomorrow=datetime.date(year,month,day)+datetime.timedelta(days=1)
print(tomorrow)

# Evaluation: OK, но пользователю ничего не будет понятно -- что вводится, что выводится.