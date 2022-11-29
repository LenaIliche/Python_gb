# 3.Задайте список из k чисел последовательности 
# (1 + 1\k)^k и выведите на экран их сумму.

input_k = int(input("Введите число k: "))

list = []
result = 0
k = 1

for i in range(input_k):
    result = (1 + 1/k)**k
    k += 1
    list.append(result)
print(list, end = "\n")
print(sum(list))