def fib(a):
    ar=[0,1]
    for i in range(1,a+1):
        if i==(ar[len(ar)-1]+ar[len(ar)-2]):
            ar.append(i)
    # print(ar)
    if ar[len(ar)-1]==a:
        return a
    else:
        return 0

if fib(25)==0:
    print("- не является числом Фибоначчи")
else:
    print("- число Фибоначчи")