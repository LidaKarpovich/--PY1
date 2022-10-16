salary = 5000  # зарплата
spend = 6000  # траты
months = 2  # количество месяцев
increase = 0.03  # рост цен
current = salary - spend
need_money = 0  # количество денег, чтобы прожить 10 месяцев
while months <= 10:
    re = salary - (spend * ((increase + 1) ** (months - 1)))
    current += re
    months += 1
need_money = -current
print(round(need_money))





