# 2.Для натурального n создать список, 
# состоящий из элементов последовательности 3n + 1

# Пример:
# - Для n = 6: [4, 7, 10, 13, 16, 19]

def progres (n):
    list = []
    for i in range (1,n+1):
        list.append(3*i+1)
    return list

num = int(input ("Веедите число N "))
result = progres(num)
print (f'{num} -> {result}')