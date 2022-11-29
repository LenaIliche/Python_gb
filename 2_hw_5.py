# 5. Реализуйте алгоритм перемешивания списка.

import random

numb = int(input("Введите кол-во элементов в списке: "))
arr_1 = list(range(numb))

print(f"Исходный список {arr_1}")

random.shuffle(arr_1)
print(f"Перемешанный список {arr_1}")