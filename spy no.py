a=1412
b=str(a)
s=0
p=1
for i in b:
    s+=int(i)
    p*=int(i)
if s==p:
    print("spy number")
else:
    print("not a spy number")
