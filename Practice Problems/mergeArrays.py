def mergearray(a,b):
    m=len(a)
    i=0
    j=0
    a.sort()
    b.sort()
    output=[]
    while i<m and j<m:
        if a[i]<b[j]:
            output.append(a[i])
            i+=1
        else:
            output.append(b[j])
            j+=1
    while i<m:
        output.append(a[i])
        i+=1
    while j<m:
        output.append(b[j])
        j+=1
    print(output)
mergearray([4,9,6,2],[9,7,10,11])
