box=[]
for i in range(6):
    ls=[int(num) for num in input().strip().split(' ')]
    box.append(ls)
for i in box:
    print(i)
result=[]
for x in range(4):
    for y in range(4):
        s=sum(box[x][y:y+3])+box[x+1][y+1]+sum(box[x+2][y:y+3])
        result.append(s)
print(max(result))

