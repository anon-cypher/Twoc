def rep(ar):
    res = ar[-1]
    ar[-1] = -1
    for i in range (len(ar)-2,-1,-1):
        temp = ar[i]
        ar[i] = res
        res = max(res,temp)
    print(ar)

arr = [17,18,5,6,1]
rep(arr)
