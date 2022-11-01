m=int(input())
for l in range(m):
    n=int(input())
    for j in range(n,-1,-1):
        c=0
        for k in range(1,j+1):
            if j%k==0:
                c+=1
        if c==2:
            mi=j
            break
    for j in range(n,n**2):
        c1=0
        for k in range(1,j+1):
            if j%k==0:
                c1+=1
        if c1==2:
            ma=j
            break
    r1=n-mi
    r2=ma-n
    if r1<r2:
        print(mi)
    elif r1==r2:
        print(mi)
    else:
        print(ma)