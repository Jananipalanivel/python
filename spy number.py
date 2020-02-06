a=int(input())
b=list(map(int,str(a)))
c=str(a)
d=[]
h=sum(b)
print(h)
for j in range(0,len(c)):
    e=int(c[j-2])
    f=e*int(c[j-1])
    g=f*int(c[j])
print(g)
if h==g:
    print("Spy number")
else:
    print("Not a spy number")
