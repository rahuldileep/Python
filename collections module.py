from collections import defaultdict, OrderedDict, namedtuple
d=defaultdict(list)
list1=[]
n,m = map(int, input().split())
for i in range(n):
    d[input()].append(i+1)
    print(d)
for i in range(m):
    list1=list1+[input()]
for i in list1:
    if i in d:
        print(' '.join(map(str,d[i])))
    else:
        print(-1)
color=namedtuple('color',['white','black','blue'])
c1=color(12,14,15)
print(c1.white)

d3=OrderedDict()
num=int(input())
for _ in range(num):
    item,space,quantity = input().rpartition(' ')
    d3[item]=d3.get(item,0)+int(quantity)
print(d3)
for item,quantity in d3.items():
    print(item,quantity)

d4=defaultdict()
n4=int(input())
for _ in range(n4):
    item4=input()
    d4[item4]=d4.get(item4,0)+1
print(len(d4))
for val in d4.values():
    print(val,end=' ')