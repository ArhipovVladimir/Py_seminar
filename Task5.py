num_day= int(input("введите номер дня недели: "))

def wach_day(day):
    if day > 7 or day < 1: print ("Такого дня не дели нет")
    elif day > 5: print ("это выходной")
    else: print ("будний день")

def name_day (day):
    if day > 7 or day < 1: return
    list_day = ["понедельник", "вторник","среда","четверг","пятница","суббота","воскресенье"]
    print (list_day [day-1])

wach_day(num_day)
name_day(num_day)