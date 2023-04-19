__aftor__="Замешаев Артем ИВТ-20"           #Работу выполнил 
import mod8
import numpy as np 

def test_sumstolb():
  # проверка матрицы 2x2 
  matr = np.array([[1, 2], [3, 4]]) #Наша матрица
  sum_rows = [sum(row) for row in matr]
  sum_tot = sum(sum_rows)
  exp_out = np.array([[4, 3], [2, 1]]) # ожидаемый ответ
  result = mod8.SumStolb(2, matr, sum_tot, sum_rows)
  assert np.array_equal(result, exp_out), f"Ошибка ввода \n {matr},\n Получили: \n {exp_out}, \n Ожидали: {result}"

  # проверка матрицы 3x3 
  matr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) #Наша матрица
  sum_rows = [sum(row) for row in matr]
  sum_tot = sum(sum_rows)
  exp_out = np.array([[28, 26, 24], [22, 20, 18], [16, 14, 12]]) # ожидаемый ответ
  result = mod8.SumStolb(3, matr, sum_tot, sum_rows)
  assert np.array_equal(result, exp_out), f"Ошибка ввода \n{matr},\n Получили: \n {exp_out}, \n Ожидали: {result}"


# создание случайной матрицы 
matr = np.random.randint(low=0, high= 20, size=(3, 3))
print(f"Заданная матрица:\n {matr}")
n=len(matr)
sum_rows=[sum(row) for row in matr]
sum_tot=sum(sum_rows)
print("Полученная матрица")
res = mod8.SumStolb(n,matr,sum_tot,sum_rows)
#вывод матрицы построчно
for row in res:
    for val in row:
        print(val, end=' ')
    print()
test_sumstolb()