def perfect(array):
    for i in range(1,len(array)-1):
        left=0
        right=0
        for j in range(i):
            left+=array[j]
        for j in range(i+1,len(array)):
            right+=array[j]
        if left==right:
            return True
    return False
print(perfect([1,2,9,8,5,7]))
