def F(n):
    if n<0:
        print("Incorrect input")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return F(n-1)+F(n-2)

print(F(5))

#another version
a,b = 0, 1
max = 0
for i in range(0, 10):
	if max < a:
		max = a
	print (a, end=" ")
	a, b = b, a + b

print ("\n max # is: ", max)

#fibonacci using generators
def fib(num):
	a, b = 0, 1
	for i in range (0, num):
		yield "{}: {}".format(i+1, a)
		a, b = b, a + b

for item in fib(10):
	print (item)