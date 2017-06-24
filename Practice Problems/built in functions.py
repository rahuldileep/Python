print('map function')
temp = [0,25,56,90]
print(map(lambda T:(5.0/9)*T +32,temp))


print('reduce function')
print(reduce(lambda x, y: x+y, temp))

print 'filter function'
print(filter(lambda x: x%2==0 ,temp))

print 'Zip Function'
l1 = [1,2,3,4]
l2 = [5,6,7,8]
z = zip(l1,l2)
print (z)
for p in z:
    print (max(p))
print(map(lambda pair: max(pair), zip(l1,l2)))

d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}
print (zip(d1,d2))

print 'switching dictionary values'
print (zip(d1,d2.itervalues()))

def switchroo(d1,d2):
    dout = {}
    for d1key, d2val in zip(d1,d2.itervalues()):
        dout[d1key] = d2val
    print(dout)
switchroo(d1,d2)

print 'enumerate function'
for count, item in enumerate(temp):
    print count
    print item

print 'assesment test'
def word_length(phrase):
    return list(map(len,phrase.split()))

print(word_length('How long are the words in this phrase'))

def digits_to_num(digits):
    print (reduce(lambda x,y : x*10 + y, digits))
digits_to_num([3,4,3,2,1])

def filter_words(word_list, letter):
    print (filter(lambda lt:lt[0]==letter,word_list))
l = ['hello','are', 'cat', 'dog', 'ham', 'hi', 'go', 'to', 'heart']
filter_words(l,'h')

def concatinate(L1, L2, connector):
    print ([w1+connector+w2 for (w1,w2) in zip(L1,L2)])
concatinate(['A','B'],['a','b'],'-')

def d_list(L):
    dict = {}
    for count,item in enumerate(L):
        dict[item] = count
    print (dict)
d_list(['a','b','c'])

def count_match_index(L):
    c=0
    for count,item in enumerate(L):
        if count == item:
            c+=1
    print(c)
count_match_index([0,2,2,1,5,5,6,10])
