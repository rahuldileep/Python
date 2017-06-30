def election_winner(L):
    d={}
    for item in L:
        d[item]=d.get(item,0)+1
    maxv=0
    val=[]
    for k,v in d.items():
        val.append(v)
    maxv=max(val)
    out=[]
    for k,v in d.items():
        if v==maxv:
            out.append(k)
    print(sorted(out)[-1])
l=[]
for i in range(int(input())):
    l.append(input())
election_winner(l)
