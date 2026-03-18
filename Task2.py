m = 20000  # подушка безопасности
s = 5000   # зарплата
p = 6000   # траты первого месяца
i = 0.05   # ежемесячный рост цен

months = 0
current_p = p
current_m = m

while current_m + s >= current_p:
    current_m = current_m + s - current_p
    months += 1
    current_p = current_p * (1 + i)

print("Количество месяцев, которое можно протянуть без долгов:", months)