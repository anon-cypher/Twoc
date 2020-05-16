num = int(input("Enter the  Number:"))
a,b = 0,1
for i in range(num):
    print(a)
    c = a + b
    a = b
    b = c
