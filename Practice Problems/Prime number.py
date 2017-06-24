flag=0
n=int(input("Enter any number greater than 1:"))
if n==2:
	flag=0
else:
	for i in range(2,n):
		if(n%i==0):
		 	flag=1
			break		
if flag==0:
	print("Prime")
else:
	print("Non prime")
