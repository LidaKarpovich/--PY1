money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
current = money_capital + salary - spend
month = 0  # количество месяцев, которое можно прожить
while current >= 0:
    re = salary - (spend + (spend * increase) ** month)
    current = money_capital + re
    month += 1
print(month)


