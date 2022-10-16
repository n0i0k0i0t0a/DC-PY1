money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0  # количество месяцев, которое можно прожить

# Ясно, что расходы превышают доходы, поэтому стоит рассматривать только как изменяется подушка безопасности
while money_capital > 0:
    spend *= (increase + 1) ** month
    money_capital += salary - spend
    month += 1

print(month)

