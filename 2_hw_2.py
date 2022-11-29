# 2. Напишите программу, которая принимает на вход число N 
# и выдает набор произведений чисел от 1 до N.

num_N = int(input ("Введите любое целое положительное число: "))

list = []
result = 1
for i in range (num_N):
    result *= (i + 1)
    list.append(result)
print(list)