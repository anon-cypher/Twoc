def dup(s):
    out=""
    for i in s:
        if i not in out:
            out+=i
    print(out)

s = input("Enter the String:")
dup(s)
