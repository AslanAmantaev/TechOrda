def res(a):
    ar =[]
    for i in range(1,a):
        if a%i==0:
            ar.append(i)
    s=0
    for i in ar:
       s+=i
    if s==a:
        return s
    else:
        return 0

if res(int(input()))>0:
    print("- Совершенное число")
else:
    print("- Несовершенное число")