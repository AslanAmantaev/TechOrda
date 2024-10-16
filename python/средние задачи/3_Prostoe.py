def res(a):
    if a<=1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a%i==0:
            return False
    return True
b = int(input("Введите число: "))
if res(b):
    print(b, "Число является простым")
else:
    print(b, "Число НЕ является простым")