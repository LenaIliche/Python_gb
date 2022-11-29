# 4. Задайте список из N элементов, заполненных 
# числами из промежутка [-N, N]. Найдите произведение элементов 
# на указанных пользователем через пробел позициях.

import random
num_N = int(input("Введите число N: "))

list = []
for i in range(num_N):
    n = random.randint((-1 * num_N), (num_N))
    list.append(n)
print(list)

mult = 1
arrange = input("Введите индексы нужных позиций: ").split()
for j in range (len(arrange)):
    arrange[j] = int(arrange[j])
    mult *= list[arrange[j]]
print(mult)