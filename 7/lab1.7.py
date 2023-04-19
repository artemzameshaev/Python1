__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил  
import mod7

def test():
    # Проверка если n= 1
    exp_out = 0 # ожидаемый ответ
    result = mod7.Calculate(1) # расчет по функции
    assert result == exp_out, f"Ошибка ввода n=1: {exp_out}, Ожидали: {result}"

    # Проверка если n= 3
    exp_out = 14 # ожидаемый ответ
    result = mod7.Calculate(3) # расчет по функции
    assert result == exp_out, f"Ошибка ввода n=3: {exp_out}, Ожидали: {result}"

    # Проверка если n = 5
    exp_out = 130  # ожидаемый ответ
    result = mod7.Calculate(5)  # расчет по функции
    assert result == exp_out, f"Ошибка ввода n=5: {exp_out}, Ожидали: {result}"


#вызов функций
n = int(input("Введите n "))
s=mod7.Calculate(n)
print(f"сумма =  {s}")
test()

