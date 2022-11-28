n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
c=[]
k=n//2
if n%2==1:
    k+=1
for i in range(k):
    a.append(l[i])
for i in range(n-1,k-1,-1):
    b.append(l[i])
if n%2==1:
    b.append(0)
for i in range(k):
    c.append(a[i])
    c.append(b[i])
print(*c)