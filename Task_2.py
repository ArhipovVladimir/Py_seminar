# Вывести на экран числа от -N до N.

a = int(input("введите число: ")) 
for num in range (-a, a+1,):
    print (f'{num} ', end='')