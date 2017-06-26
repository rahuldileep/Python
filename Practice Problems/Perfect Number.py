n=int(input('Enter the number you want to check:'))
sum=0
for i in range(1,n):
    if n%i==0:
        sum+=i
if sum==n:
    print('Yes, it is a perfect number.')
else:
    print('No, it is not a perfect number.')
