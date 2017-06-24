def mergesort(A):
    n=len(A)
    if n<2:
        return
    else:
        m=n//2
        L=A[:m]
        R=A[m:]
        mergesort(L)
        mergesort(R)
        merge(L,R,A)
    return A
def merge(L,R,A):
    ll=len(L)
    lr=len(R)
    i=j=k=0
    while i<ll and j<lr:
        if L[i]<R[j]:
            A[k]=L[i]
            i+=1
        else:
            A[k]=R[j]
            j+=1
        k+=1
    while i<ll:
        A[k]=L[i]
        i+=1
        k+=1
    while j<lr:
        A[k]=R[j]
        j+=1
        k+=1
print(mergesort([5,2,4,6,1,0,3,7]))
