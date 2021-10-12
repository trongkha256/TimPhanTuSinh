def ucln(a, b):
    if (b == 0):
        return a
    return ucln(b, a % b)

def TimPTS(p):
    a = []
    for i in range (1,p):
        if ucln(p,i)==1:
            a.append(i)
    k=len(a)
    d = []
    for i in range (1,p):
        d.append(0)
    for i in range (0,k):
        d[a[i]] = 1
    t = 1
    for i in range(0, p):
        t = (t*a[i]) % p
        d[t]=d[t]-1
    check = []
    for i in range (0,k):
        check.append(1)
    for i in range(1,k):
        if d[a[i]]>0:
            check[i]=0
    for i in range (0,k):
        if check[i]==1:
            print(a[i]," ")
TimPTS(29)





