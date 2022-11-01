n=int(input())
p=[]
for i in range(2,n+1):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c+=1
    if c==2:
        p.append(i)
d=0
for i in range(len(p)):
    for j in range(i+1,len(p)):
        if p[i]*p[j]==n:
            print(p[i],end=" ")
            print(p[j])
            d+=1
            break
if d==0:
    print("-1")