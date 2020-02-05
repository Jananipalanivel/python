n=int(input())
a=str(n)
j=len(a)
b=[]
for i in range(len(a)):
    c=int(a[i])
    b.append(c)
d=sum(b)
if j>=2:
    e=d**j
    print(e)
else:
    print(n)
