__aftor__="Замешаев артем ивт-20"
"""Даны два действительных числа. Вывести первое число, если оно больше второго, и оба числа, если это не так"""
def test():
    # тест если num1 > num2
    expected_output = "num1 > num2 | 3.0\n"
    num1 = 3.0
    num2 = 2.0
    result = compare_numbers(num1, num2)
    assert result == expected_output, f"Ошибка ввода ({num1}, {num2}), Ожидалось: {expected_output}, Получили: {result}"

    # тест если num1 < num2
    expected_output = "num1 <,= num2 | 2.0 | 3.0\n"
    num1 = 2.0
    num2 = 3.0
    result = compare_numbers(num1, num2)
    assert result == expected_output, f"Ошибка ввода ({num1}, {num2}), Ожидалось: {expected_output}, Получили: {result}"

    # тест если num1 = num2
    expected_output = "num1 <,= num2 | 4.0 | 4.0\n"
    num1 = 4.0
    num2 = 4.0
    result = compare_numbers(num1, num2)
    assert result == expected_output, f"Ошибка ввода ({num1}, {num2}), Ожидалось: {expected_output}, Получили: {result}"
# сравнение чисел
def compare_numbers(num1, num2):
    if num1 > num2:
        return f"num1 > num2 | {num1}\n"
    else:
        return f"num1 <,= num2 | {num1} | {num2}\n"



num1 = float(input("Введите первое число "))
num2 = float(input("Введите второе число "))
if num1 > num2:
    print(f"num1 > num2 | {num1}")
else:
    print(f"num1 <,= num2 | {num1} | {num2} ")

test() # функция теста 