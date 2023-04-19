__aftor__="Замешаев артем ивт-20"
import math

def test():
    cathet1 = 3
    cathet2 = 4

    # Тестовый расчет гипотенузы
    res_hyp = 5.0  #ответ
    actual_hyp = math.sqrt(cathet1**2 + cathet2**2) # актуальный ответ
    assert actual_hyp == res_hyp, f"Гипотенуза должна быть не {res_hyp}, а {actual_hyp}"

    # Тестовый расчет площади
    res_area = 6.0 #ответ
    actual_area = (cathet1 * cathet2) / 2 # актуальный ответ
    assert actual_area == res_area, f"Площадь должна быть не {res_area}, а {actual_area}"



cathet1 = int(input("Введите первый катет: "))
cathet2 = int(input("Введите второй катет: "))
# поиск гипотинузы
hypotenuse = math.sqrt(cathet1**2 + cathet2**2)
print(f"Гипотинуза: {hypotenuse}")
# поиск площади
area = (cathet1 * cathet2) / 2
print(f"Площадь: {area}")

test() #вызов функции теста