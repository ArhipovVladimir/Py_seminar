a =[1,18,12,1155,188]

def find_max_num (list):
    max = list [0]
    for num in list:
        if num > max:
            max =num
    return max

print (find_max_num(a))    
444
