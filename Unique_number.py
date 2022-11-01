n=input()
a=[]
for i in n:
    if i.isdigit:
        if i not in a:
            a.append(i)
if len(a)==len(n):
    print("Unique Number")
else:
    print("Not Unique Number")