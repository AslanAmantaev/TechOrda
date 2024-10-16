def res(a,b,c):
    if a>=b  and a>=c:
        return a
    elif b>=a and b>=c:
        return b
    else:
        return c
a=int(input("Введите a:"))
b=int(input("Введите b:"))
c=int(input("Введите c:"))
print(res(a, b, c))