a=int(input())
b=a*a
print(b)
d=str(b)
e=len(d)
f=e//2
print(f)
g=d[:f]
print(g)
h=d[f:]
print(h)
i=int(g)
j=int(h)
k=i+j
print(k)
if k==a:
    print("Kepreker Number")
else:
    print("Not a kerpreker Number")
