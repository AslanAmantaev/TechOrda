def res(b:float,k:float,n:int):
    for i in range(n):
        b+=b*k/100
    print(b)
b=int(input("Введите баланс:"))
k=int(input("Введите процент:"))
n=int(input("Введите срок:"))
res(b,k,n)
