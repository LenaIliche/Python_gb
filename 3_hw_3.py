# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением 
# дробной части элементов.

import math

arr = list(map(float, input("Введите вещественные числа списка через пробел: ").split()))

frac_numb = 0
whole_numb = 0
frac_arr = []

for i in range (len(arr)):
    frac_numb, whole_numb = math.modf(arr[i])
    frac_arr.append(round (frac_numb,3))
print(frac_arr)

diff = max(frac_arr) - min(frac_arr)
print(diff)
