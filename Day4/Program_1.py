def count(t):
    for i in t:
        c=0
        for j in t:
            if i==j:
                c+=1
        print(i,"-",c)

t = (1,2,3,4,5,2,2,3,6)
count(t)
