import timeit
def fibonacci_One(n):
	a, b=0, 1
	for i in range(n):
		nex=a+b
		if i <= 1:
			print i
		else:
			print nex
			a, b = b, nex		

def fibonacci_Two(n):
	if n==0:
		return 0
	if n==1:
		return 1
	return fibonacci_Two(n-1) + fibonacci_Two(n-2)


def fibonacci_Three(n):
	a,b=0,1
	for i in range(n):
		a,b = b,a+b
                print a

def fibonacci_Four():
	a,b=0,1
	while True:
		yield a
		a,b=b,a+b


print 'Differt methods to print Fibonacci Series in Python'

n=int(input('enter the number:'))
print '\n*# Method One #*'
s_time_1=timeit.default_timer()
fibonacci_One(n)
e_time_1=timeit.default_timer() - s_time_1
print '\n Exec_Time for method One =',e_time_1,'Seconds'

print '\n*# Method Two #*'
s_time_2=timeit.default_timer()
for i in range(n):
	print fibonacci_Two(i)	
e_time_2=timeit.default_timer() - s_time_2
print '\n Exec_Time for method Two =',e_time_2,'Seconds'
print '\n*# Method Three #*'
s_time_3=timeit.default_timer()
for i in range(n):
	fibonacci_Three(i)
e_time_3=timeit.default_timer() - s_time_3
print '\n Exec_Time for method Three =',e_time_3,'Seconds'
print '\n*# Method Four #*'
s=0
s_time_4=timeit.default_timer()
for i in fibonacci_Four():
	if s >=n:
		break
	print i
	s+=1
e_time_4=timeit.default_timer() - s_time_4
print '\n Exec_Time for method Four =',e_time_4,'Seconds'



