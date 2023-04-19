__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 

    # суммы столбцов
def SumStolb(n,matr,sum_tot,sum_rows):
    sum_cols=[]
    for i in range(n):
        s=0
        for j in range(n):
            s+=matr[j][i]
        sum_cols.append(s)

    # результат
    res=[[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            res[i][j]=sum_tot-sum_rows[i]-sum_cols[j]+matr[i][j]
    return res
