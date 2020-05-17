def isec(l1,l2):
    l3=[]
    for i in l1:
        for j in l2:
            if i == j:
                l3.append(i)
    return l3
def dup(l3):
    out=[]
    for i in l3:
        if i not in out:
            out.append(i)
    print(out)

l1 = [1,2,3,4,2,5]
l2 = [2,3,1,1,6]
l3 = isec(l1,l2)
dup(l3)
