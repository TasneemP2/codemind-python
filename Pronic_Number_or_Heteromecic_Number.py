import math

Number = int(input())

i = 0
flag = 0

while i <= (int) (math.sqrt(Number)):
    if Number == i * (i + 1):
        flag = 1
        break
    i = i + 1

if flag == 1:
    print("YES")
else:
    print("NO")