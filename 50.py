n=input()
a=int(input())
b=str(a)
c=len(n)
e=n[-1]
h=b[0]
while a>9:
    a=sum(list(map(int,str(a))))
    d=a
j=str(d)
f=n[0]
if f.isupper()==True:
    g=f.swapcase()
    print(h+g+j+e)
if f.islower()==True:
    k=f.swapcase()
    print(h+k+j+e)
