money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
months_ = 1     # Количество месяцев без долгов
n = 0
while spend < salary + money_capital:
    money_capital = money_capital + salary - spend * (1 + increase * n)
    months_ += 1
    n += 1
    spend = spend * (1 + increase)
print("Количество месяцев, которое можно протянуть без долгов:", months_)

