def test():
    # конь угрожает полю
    exp_out = "Угрожает\n" # ожидаемый ответ
    k = 1
    l = 1
    m = 3
    n = 2
    result = check(k, l, m, n)
    assert result == exp_out, f"Ошибка ввода ({k}, {l}, {m}, {n}), Ожидание: {exp_out}, Получили: {result}"

    # конь не угрожает полю
    exp_out = "Не угрожает\n" # ожидаемый ответ
    k = 1
    l = 1
    m = 4
    n = 2
    result = check(k, l, m, n)
    assert result == exp_out, f"Ошибка ввода ({k}, {l}, {m}, {n}), Ожидание: {exp_out}, Получили: {result}"

#проверка на угрозу
def check(k, l, m, n):
    if ((abs(abs(k-m)-2)<0.5) and (abs(abs(l-n)-1)<0.5)  or (abs(abs(k-m)-1)<0.5) and (abs(abs(l-n)-2.0)<0.5)):
        return "Угрожает\n"
    else:
        return "Не угрожает\n"


k = int(input("Введите номер вертикали первой фигуры "))
l = int(input("Введите номер горизонтали первой фигуры "))
m = int(input("Введите номер вертикали коня "))
n = int(input("Введите номер горизонтали коня "))
if ((abs(abs(k-m)-2)<0.5) and (abs(abs(l-n)-1)<0.5)
    or (abs(abs(k-m)-1)<0.5) and (abs(abs(l-n)-2.0)<0.5)):
    print('Угрожает')
else:
    print('Не угрожает')

test()
