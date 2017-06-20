def factorial(n):
    for i in range(n-1):
	return n * factorial(n-1)
print('enter any number')
i=int(input())
x=factorial(i)
print('The factorial of the num is '+str(x))
