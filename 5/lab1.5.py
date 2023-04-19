__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 
import mod5

def test():
    # тест если n=5
    expected_output = 2*(sum([1,2,3,4,5]))**2  #ожидаемый ответ 
    mas = [1, 2, 3, 4, 5]  # наш массив
    result = mod5.Calculation(mas)
    assert result == expected_output, f"Ошибка ввода {mas}, Ожидали: {expected_output}, Получили: {result}"
    # тест если n=10
    expected_output = 2*(sum([5,4,7,1,9,11,7,4,18,2]))**2 #ожидаемый ответ 
    mas = [5, 4, 7, 1, 9, 11, 7, 4, 18, 2]  # наш массив
    result = mod5.Calculation(mas)
    assert result == expected_output, f"Ошибка ввода {mas}, Ожидали: {expected_output}, Получили: {result}"


n = int(input("Введите n: "))
#вызов функций
mas = []
mod5.InputMass(n, mas)
print(f"Наш массив {mas}")
print(f"Расчет по формуле 2(a1+...+an)^2 = {mod5.Calculation(mas):.4f}")

test()