def test():
    # тест если n=3
    exp_out = "Результат: 0.75"
    n = 3
    result = check(n)
    assert result == exp_out, f"Ошибка ввода {n}, Ожидали: {exp_out}, получили: {result}"

    # тест если n=8
    exp_out = "Результат: 0.8888888888888888"
    n = 8
    result2 = check(n)
    assert result2 == exp_out, f"Ошибка ввода {n}, Ожидали: {exp_out}, получили: {result2}"
#проверка расчета
def check(n):
    res = 1
    for i in range(2, n):
        res = 1
        res = res * ((i+1) / (i+2))
    return f"Результат: {res}"



n = int(input("Введите n "))
for i in range(2, n):
  res = 1
  res = res* ((i+1) / (i+2))
print(f"Результат: {res}")

test()  #проверка