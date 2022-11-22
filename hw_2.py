# Напишите программу для. проверки истинности 
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для 
# всех значений предикат.

x = int(input('Введите значение Х: '))
y = int(input('Введите значение У: '))
z = int(input('Введите значение Z: '))

for x in [0, 1]:
    for y in [0, 1]:
        for z in [0, 1]:
            result = not (x or y or z) == ((not x) and (not y) and (not z))
            print(f'if X = {x}, Y = {y}, Z = {z} then result = {result}')