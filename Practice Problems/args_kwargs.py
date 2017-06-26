def func(*args,**kwargs):
    for arg in args:
        print(arg)
    for item in kwargs.items():
        print(item)
func(1,2,3,4,5,5,6,6,6,7,7,7,7,7,a=10,b=20,c=30)
