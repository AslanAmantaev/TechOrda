def miss_you(array1,array2):
    res=[]
    for i in range(len(array2)):
        for j in range(len(array1)):
            if array2[i]==array1[j]:
                break
            if j==len(array1)-1:
                res.append(array2[i])
    print(sorted(res))
miss_you([1,1,3,2,5],[1,3,9,5,7])
