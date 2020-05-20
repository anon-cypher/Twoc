num = list(map(int,input().split()))
l_o = []
l_e = []
for i in num:
    if i%2==0:
        l_e.append(i)
    else:
        l_o.append(i)

l_o.sort(reverse=True)
l_e.sort()

f_list = l_o+l_e
print(f_list)
