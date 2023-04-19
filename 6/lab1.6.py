__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 
import mod6

def test():
    # входное значение [1, 2, 3, 4, 5]
    exp_out = 3  # ожидаемый результат
    input_value = [1, 2, 3, 4, 5]  # входное значение
    result = mod6.Calculation(input_value)
    assert result == exp_out, f"Ошибка ввода {input_value}, Ожидали: {exp_out}, Получили: {result}"

    # входное значение [5, 4, 7, 1, 9, 11, 7, 4, 18, 2]
    exp_out = 4  # ожидаемый результат
    input_value = [5, 4, 7, 1, 9, 11, 7, 4, 18, 2]  # входное значение
    result = mod6.Calculation(input_value)
    assert result == exp_out, f"Ошибка ввода {input_value}, Ожидали: {exp_out}, Получили: {result}"




#вызов функций 
n = int(input("Введите размер массива: "))
mas = mod6.RandMass(n)
print(f"Наш массив: {mas}")
print(f"количество членов ak последовательности: {mod6.Calculation(mas)}")
test()
