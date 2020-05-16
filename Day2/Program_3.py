num = int(input("Enter the Number:"))
for i in range(num):
	s=' '*i+'*'+' '*(num-i-1)
	print(s+s[::-1])
for i in range(num):
	s=' '*(num-i-1)+'*'+' '*i
	print(s+s[::-1])
