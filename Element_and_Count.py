n=int(input())
l=list(map(int,input().split()))
a=[]
b=[]
d=[]
for i in l:
    if i not in a:
        c=l.count(i)
        a.append(i)
        b.append(c)
for i in range(len(a)):
    d.append(a[i])
    d.append(b[i])
print(*d)