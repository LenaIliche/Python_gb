# 5. Задайте число. Составьте список чисел Фибоначчи, 
# в том числе для отрицательных индексов.

# num_k = int(input("Задайте число k: "))

# arr_fib=[]
# fib1 = 1
# fib2 = 1

# arr_fib.append(fib1)
# arr_fib.append(fib2)

# for i in range(2, num_k):
#     fib1, fib2 = fib2, fib1 + fib2
#     arr_fib.append(fib2)

# print(arr_fib)

# arr_fib_rev = []
# count = 0

# for j in reversed(arr_fib):
#     count += 1
#     if (len(arr_fib) % 2) != 0:
#         if (count % 2 != 0):
#             arr_fib_rev.append(j)
#         elif (count % 2 == 0):
#             arr_fib_rev.append(-1 * j)
#     else: 
#         if (count % 2 == 0):
#             arr_fib_rev.append(j)
#         elif (count % 2 != 0):
#             arr_fib_rev.append(-1 * j)
# print(arr_fib_rev)

# arr_fib.insert(0, 0)

# arr_merged = []

# for i in arr_fib_rev: 
#     arr_merged.append(i)
# for i in arr_fib:
#     arr_merged.append(i)

# print(arr_merged)

num_k = int(input("Задайте число k: "))

arr_fib = [0]
fib1 = 0
fib2 = 1
    
for i in range (0, num_k):
    fib1, fib2 = fib2, fib1 + fib2
    arr_fib.append(fib1)

arr_fib_rev = arr_fib.copy()
del arr_fib_rev[0]
arr_fib_rev.reverse()

while len(arr_fib_rev) > 0:
    arr_fib.insert(0, arr_fib_rev.pop())
    if len(arr_fib_rev) > 0:
        arr_fib.insert(0, (-1 * arr_fib_rev.pop()))
print(arr_fib)