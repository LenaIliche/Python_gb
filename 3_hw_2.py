# 2. Напишите программу, которая найдёт произведение 
# пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
    
arr = list(map(int, input("Введите числа списка через пробел: ").split()))
print(arr, end = "")
arr_2 = []
while len(arr) > 1:
   arr_num = arr[0] * arr[-1]
   del arr[0]
   del arr[-1]
   arr_2.append(arr_num)
   if len(arr) == 1:
       arr_num = arr[0]**2
       arr_2.append(arr_num)
    
print(f" => {arr_2}")