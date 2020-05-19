def candidate(arr):
    li=[]
    for i in arr:
        li.append(arr[i])
    max_value = max(li)
    name=[]
    for i in arr:
        if arr[i]==max_value:
            name.append(i)
    print(name)

    small=name[0]
    for i in range(0, len(name)):
        if len(small)>len(name[i]):
            small=name[i]
    print(small)



dic = {"abhi":3,"rahul":5,"rajiv":1,"priyanka":5,"rishu":5,"chandan":5,"rani":5}
candidate(dic)
