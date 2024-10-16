def res(a, b):
    step= 1
    for i in range(b):
        step *= a
    return step
a=int(input("Введите а:"))
b=int(input("Введите b:"))
print(power(a, b))