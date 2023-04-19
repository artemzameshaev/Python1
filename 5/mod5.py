import random
__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 
def InputMass(n,mas):                      #Задаем рандомный массив
    for i in range(n):
        mas.append(random.randint(1,20))
    return mas

def Calculation(mas):                           #Расчет
    """Расчет по формуле 2(a1+...+an)^2"""
    summ = 0
    for a in mas:
        summ += a
    res= 2*(summ)**2
    return res