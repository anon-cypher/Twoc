n=int(input('Enter number:'))
for i in range(n):
	x='* '*(n-i)+'  '*i
	print(x+x[::-1])

for i in range(1,n+1):
	y='* '*i+'  '*(n-i)
	print(y+y[::-1])
