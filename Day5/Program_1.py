def rep(x,y,z):
    x=str(x)
    out = x.replace(y,z)
    print(int(out))

num = int(input("Enter the number:"))
y = input("Enter the value that you want to replace:")
z = input("Enter the value with whom you want to replace:")
rep(num,y,z)
