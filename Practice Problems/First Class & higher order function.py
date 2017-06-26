def square(x):
    return x**2
def cube(x):
    return x**3
def my_map(func,arr):
    result=[]
    for item in arr:
        r=func(item)
        result.append(r)
    print(func.__name__)
    return result
s=square
print('First Class function:',s.__name__,'|| Output:',s(100))
output=my_map(square,[1,2,3,4,5])
print(output)
output2=my_map(cube,[1,2,3,4,5])
print(output2)


def htmltag(tag):
    def message(msg):
        print('<{0}><{1}><{0}>'.format(tag,msg))
    return message
print('\n')
print_h1 = htmltag('h1')
print_h1('Headline')
print_h1('Next Headline')
