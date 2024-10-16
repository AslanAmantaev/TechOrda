# def res(n):
#     return (n*(n+1)*(2*n+1))//6
# n=int(input("Введите "))
# print(res(n))
# from ipaddress import summarize_address_range

n=int(input("Введите n:"))
summ=0
for i in range(1,n+1):
    summ+=i**2

print("Сумма квадратов последовательных чисел до",n,"равна:",summ)
