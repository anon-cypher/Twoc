def rdic(a):
    value = a.values()
    l = []
    for i in value:
        if i not in l:
            l.append(i)
    print(l)
    

x = {"a":1,"b":2,"c":1}
rdic(x)
