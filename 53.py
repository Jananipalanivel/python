import math
a=int(input())
b=str(a)
c=[]
d=[]
for i in range(len(b)):
    c.append(int(b[i]))
    d.append(math.factorial(c[i]))
    e=sum(d)
if e==a:
    print("Strong number")
else:
    print("Not a strong number")
    
    
