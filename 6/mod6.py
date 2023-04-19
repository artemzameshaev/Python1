import random
__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 

def RandMass(n):  
    mas= []                        #Задаем рандомный массив
    for i in range(n):
        mas.append(random.randint(1,20))
    return mas

def Calculation(mas):                               #Расчет количество членов ak последовательности
    """имеющих четные порядковые номера и являющихся нечтными числами"""
    elem = 0
    otve = 0
    for elem in mas[::2]:
        if elem % 2 :
            otve += 1
    return otve