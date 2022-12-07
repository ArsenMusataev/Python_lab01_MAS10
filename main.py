import math
try:
    a = float(input("Введите А ="))
    b = float(input("Введите В ="))
    x = float(input("Введите Х ="))
    y = ''
    try:
        if x > 4:
            y = (5) * (x * x) + (b * b) / (a * a) + (b * b)
        else:
            y = (6) * ((x * x) - (a * a))
        print("Ответ =",format(y, "#.2f"))
    except ZeroDivisionError:
        print("Нет решения!")
except:
    print("Неверные входные данные!")
