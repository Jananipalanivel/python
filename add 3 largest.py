a=list(map(int,input().split()))
b=list(map(int,input().split()))
c=list(map(int,input().split()))
d=list(map(int,input().split()))
e=list(map(int,input().split()))
a1=sorted(a)
b1=sorted(b)
c1=sorted(c)
d1=sorted(d)
e1=sorted(e)
a2=a1[5:1:-1]
b2=b1[5:1:-1]
c2=c1[5:1:-1]
d2=d1[5:1:-1]
e2=e1[5:1:-1]
a3=str(a2[0])+str(a2[1])+str(a2[2])
a4=int(a3)
b3=str(b2[0])+str(b2[1])+str(b2[2])
b4=int(b3)
c3=str(c2[0])+str(c2[1])+str(c2[2])
c4=int(c3)
d3=str(d2[0])+str(d2[1])+str(d2[2])
d4=int(d3)
e3=str(e2[0])+str(e2[1])+str(e2[2])
e4=int(e3)
print(a4+b4+c4+d4+e4)
