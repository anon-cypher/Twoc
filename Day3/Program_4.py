def dup(l):
    out=[]
    for i in l:
        if i not in out:
            out.append(i)
    print(out)

# Taking list of my choice as it is not mentioned in the problem to create a list also
li = [1,2,2,3,1,5]
dup(li)
