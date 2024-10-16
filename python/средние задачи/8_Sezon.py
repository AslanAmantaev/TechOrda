def res(month, day):
    if (month==12 and day<=31) or (month==1 and day<=31) or (month==2 and day<=28):
        return "Зима"
    elif (month==3 and day<=31) or (month==4 and day<=30) or (month==5 and day<=31):
        return "Весна"
    elif (month==6 and day<=30) or (month==7 and day<=31) or (month==8 and day<=31):
        return "Лето"
    elif (month==9 and day<=30) or (month==10 and day<=31) or (month==11 and day<=30):
        return "Осень"
    else:
        return "Некорректная дата"

month = int(input("Введите номер месяца: "))
day = int(input("Введите день месяца : "))
print(res(month, day))
