n=int(input())
l=n
sum=0
while n!=0:
    r=n%10
    sum=sum*10+r
    n=n//10
if sum==l:
    print("True")
else:
    print("False")