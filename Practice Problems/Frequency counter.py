file = open('SampleTextFile.txt','r')
dict_items = {}
for line in file:
    L=line.split()
    for item in L:
        dict_items[item]=dict_items.get(item,0)+1
sortedvalue_dict=sorted(dict_items.items(),key = lambda t: t[1])
l=len(sortedvalue_dict)
Last10=reversed(sortedvalue_dict[l-10:l])
for i in Last10:
    print(i[0])
