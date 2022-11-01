n=int(input())
a=n
b=n
while 1:
    f=0
    for i in range(1,a+1):
        if a%i==0:
            f+=1
    if f==2:
        fwd=a-n
        break
    a+=1
while 1:
    f=0
    for i in range(1,b+1):
        if b%i==0:
            f+=1
    if f==2:
        bwd=n-b
        break
    b-=1
if fwd==0 and bwd==0:
    print(fwd)
elif fwd<bwd:
    print(fwd)
else:
    print(bwd)