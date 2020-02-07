a=input()
b=input()
c=input()
d=int(input())
e=len(a)
f=len(b)
if e>f:
    a1=a[0]
    c1=a1+b
    c2=c1.swapcase()
if e<f:
    a1=b[0]
    c1=a1+a
    c2=c1.swapcase()
a3=a[0]
a4=b[0]
x=ord(a3)
y=ord(a4)
if e==f and a3<a4:
    a1=b[0]
    c1=a1+a
    c2=c1.swapcase()
elif e==f and a3>a4:
    a1=a[0]
    c1=a1+b
    c2=c1.swapcase()
c3=c[d-1]
y=list(c)
y.reverse()
c4=y[d-1]
print(c2+c3+c4) 
