def res(a,b):
    if a>b:
        return 1
    elif a==b:
        return 0
    else:
        return -1
a=int(input("Введите a:"))
b=int(input("Введите b:"))
print(res(a,b))