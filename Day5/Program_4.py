x=[[200,1],[100,2],[250,3],[190,7]]
w=500
sum = 0
l = []
for i in x:
    if (sum+i[0]) >w:
        continue
    else:
        sum+=i[0]
        l.append(i[1])
print(sum)
print(l)
