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

arr=[]
for i in range(0,1001):
    s=res(i)
    if s>0:
        arr.append(s)

print(arr)
