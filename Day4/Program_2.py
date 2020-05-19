def s(t):
    l1 = list(t)
    # l2 = l1.sort()
    # out = tuple(l2)
    l1.sort()
    l2 = tuple(l1)
    print(l2)

t = (3,1,2,4)
s(t)
