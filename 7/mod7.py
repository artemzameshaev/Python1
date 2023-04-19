__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 

def Calculate(n):  
    """Функция по расчету суммы по формуле https://ivtipm.github.io/Programming/Glava10/index10.htm#z335"""
    s = 0
    for k in range(1,n):
        c= (k+1)*k*k
        s+= c
    return s