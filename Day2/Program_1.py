def isOdd(n):
    if n%2==0:
        print("Even")
    else:
        print("Odd")

def isPrime(n):
    count=0
    for i in range(2,n//2):
        if n%i==0:
            count+=1
    if count==0:
        print("Prime")
    else:
        print("Not Prime")

def isPalindrome(n):
    s = str(n)
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# for 3-digit numbers
def isArmstrong(n):
    s = str(n)
    c = 0
    for i in s:
        c += int(i)**3
    if c==n:
        print("Armstrong")
    else:
        print("Not Armstrong")

num = int(input("Enter the Number:"))
isOdd(num)
isPrime(num)
isPalindrome(num)
isArmstrong(num)
