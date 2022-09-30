# 1.Напишите программу, которая принимает
#  на вход число N и выдаёт последовательность из N
# членов.

# Пример:
# - Для N = 5: 1, -3, 9, -27, 81



def progres (n):
    list = [1]
    for i in range (1,n):
        list.append(list[i-1]*-3)
    return list

num = int(input ("Веедите число N "))
result = progres(num)
print (f'{num} -> {result}')
